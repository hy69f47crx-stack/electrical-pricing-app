import os
from pathlib import Path

# مسارات المشروع
PROJECT_ROOT = Path(__file__).parent
APP_DIR = PROJECT_ROOT / "app"
DATA_DIR = PROJECT_ROOT / "data"
TRAINING_DATA_DIR = PROJECT_ROOT / "training_data"
MODELS_DIR = PROJECT_ROOT / "models"
LOGS_DIR = PROJECT_ROOT / "logs"

# إنشاء المجالد المطلوبة
for directory in [DATA_DIR, TRAINING_DATA_DIR, MODELS_DIR, LOGS_DIR]:
    directory.mkdir(exist_ok=True)

# إعدادات قاعدة البيانات
DATABASE_PATH = DATA_DIR / "classification.db"
DATABASE_PASSWORD = "secure_password_change_me"  # يتغير عند الدخول الأول

# إعدادات التطبيق
APP_NAME = "نظام تصنيف الملفات"
APP_VERSION = "1.0.0"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
DEFAULT_TIMEOUT = 900  # 15 دقيقة (Idle timeout)

# إعدادات معالجة الملفات
PDF_EXTENSIONS = [".pdf"]
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB
SUPPORTED_FORMATS = ("*.pdf",)

# تصنيفات الملفات
MAIN_CATEGORIES = {
    "هندسي": "engineering",
    "حسابي": "financial"
}

SUB_CATEGORIES = {
    "engineering": {
        "كهربائي": "electrical",
        "مدني": "civil",
        "ميكانيك": "mechanical",
        "كمبيوتر": "computer"
    }
}

# إعدادات التصنيف الآلي
MIN_CONFIDENCE = 0.85  # الحد الأدنى للثقة (85%)
TARGET_ACCURACY = 0.95  # هدف الدقة (95%)

# إعدادات معالجة الملفات
BATCH_SIZE = 10
THREAD_POOL_SIZE = 4
WATCH_FOLDER = DATA_DIR / "watch"
WATCH_FOLDER.mkdir(exist_ok=True)

# إعدادات الإحصائيات
STATS_UPDATE_INTERVAL = 1000  # ms (كل ثانية)

# اللغة والإعدادات الإقليمية
LANGUAGE = "ar"
DATE_FORMAT = "%d/%m/%Y"
TIME_FORMAT = "%H:%M:%S"
