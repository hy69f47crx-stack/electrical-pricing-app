from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import hashlib, os, sys
from pathlib import Path
from werkzeug.utils import secure_filename
from time import time
from functools import wraps

# Add project root to sys.path so imports work from /tmp
PROJECT_DIR = Path(__file__).parent
sys.path.insert(0, str(PROJECT_DIR))

from app.core.database import DatabaseManager
from app.core.classifier import DocumentClassifier
import config

app = Flask(
    __name__,
    template_folder=str(PROJECT_DIR / "templates"),
    instance_path=str(PROJECT_DIR / "data"),
    root_path=str(PROJECT_DIR),
)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or os.urandom(32).hex()
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max upload

PASSWORD_FILE = config.DATA_DIR / ".password_hash"
db = DatabaseManager()
classifier = DocumentClassifier(config.MODELS_DIR / "classifier.pkl")

login_attempts = {}  # IP -> (count, timestamp)

def rate_limit_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        ip = request.remote_addr
        now = time()
        if ip in login_attempts:
            count, last_time = login_attempts[ip]
            if now - last_time < 300:  # 5 دقائق
                if count >= 5:
                    return jsonify({"ok": False, "msg": "حاولت أكثر من مرات. حاول لاحقاً"}), 429
                login_attempts[ip] = (count + 1, now)
            else:
                login_attempts[ip] = (1, now)
        else:
            login_attempts[ip] = (1, now)
        return f(*args, **kwargs)
    return decorated_function

def get_password_hash():
    if PASSWORD_FILE.exists():
        return PASSWORD_FILE.read_text().strip()
    return None


def save_password_hash(pw_hash):
    PASSWORD_FILE.write_text(pw_hash)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ─── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return redirect(url_for("dashboard"))


@app.route("/login", methods=["GET", "POST"])
@rate_limit_login
def login():
    if request.method == "POST":
        password = request.json.get("password", "").strip()
        if not password:
            return jsonify({"ok": False, "msg": "أدخل كلمة المرور"})

        stored = get_password_hash()
        if stored is None:
            # أول مرة: حفظ كلمة المرور والدخول مباشرة
            save_password_hash(hash_password(password))
            session["logged_in"] = True
            return jsonify({"ok": True, "first_time": True})
        elif hash_password(password) == stored:
            session["logged_in"] = True
            return jsonify({"ok": True})
        else:
            return jsonify({"ok": False, "msg": "كلمة المرور غير صحيحة"})

    is_first = get_password_hash() is None
    return render_template("login.html", is_first=is_first)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("main.html", page="dashboard")


@app.route("/upload")
def upload():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("main.html", page="upload")


@app.route("/files")
def files():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("main.html", page="files")


# ─── API ───────────────────────────────────────────────────────────────────────

@app.route("/api/stats")
def api_stats():
    if not session.get("logged_in"):
        return jsonify({"error": "unauthorized"}), 401
    return jsonify(db.get_statistics())


@app.route("/api/files")
def api_files():
    if not session.get("logged_in"):
        return jsonify({"error": "unauthorized"}), 401
    files_list = db.get_all_files()
    return jsonify([{
        "id": f.id,
        "filename": f.filename,
        "main_category": f.main_category,
        "sub_category": f.sub_category or "-",
        "confidence": round(f.confidence * 100),
        "processing_time": round(f.processing_time, 2),
        "date": f.classified_at.strftime("%d/%m/%Y %H:%M")
    } for f in files_list])


@app.route("/api/upload", methods=["POST"])
def api_upload():
    if not session.get("logged_in"):
        return jsonify({"error": "unauthorized"}), 401

    if "files" not in request.files:
        return jsonify({"ok": False, "msg": "لم يتم رفع ملفات"})

    results = []
    upload_dir = config.DATA_DIR / "uploads"
    upload_dir.mkdir(exist_ok=True)

    for file in request.files.getlist("files"):
        if not file.filename.lower().endswith(".pdf"):
            results.append({"filename": file.filename, "ok": False, "msg": "ليس PDF"})
            continue

        safe_filename = secure_filename(file.filename)
        if not safe_filename:
            results.append({"filename": file.filename, "ok": False, "msg": "اسم ملف غير صالح"})
            continue

        save_path = upload_dir / safe_filename
        file.save(save_path)

        result = classifier.classify_pdf(save_path)
        if result.get("success"):
            try:
                db.add_classified_file(
                    filename=file.filename,
                    file_path=str(save_path),
                    main_category=result["main_category"],
                    sub_category=result.get("sub_category"),
                    confidence=result["confidence"],
                    processing_time=result["processing_time"]
                )
                results.append({
                    "filename": file.filename,
                    "ok": True,
                    "main_category": result["main_category"],
                    "sub_category": result.get("sub_category", "-"),
                    "confidence": round(result["confidence"] * 100)
                })
            except Exception as e:
                results.append({"filename": file.filename, "ok": False, "msg": "خطأ في حفظ الملف"})
        else:
            results.append({"filename": file.filename, "ok": False, "msg": result.get("error", "خطأ")})

    return jsonify({"ok": True, "results": results})


@app.route("/api/delete/<int:file_id>", methods=["DELETE"])
def api_delete(file_id):
    if not session.get("logged_in"):
        return jsonify({"error": "unauthorized"}), 401
    ok = db.delete_file(file_id)
    return jsonify({"ok": ok})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, port=port, host="127.0.0.1")
