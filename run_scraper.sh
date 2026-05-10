#!/bin/bash
# ⚠️ التحديث الشهري — مرة واحدة بالشهر فقط (التزاماً بالحدود القانونية).
# لا تجدوله يومياً. السكريبر نفسه يفرض check_monthly_limit ويرفض التشغيل
# الزائد، لكن نعتمد على cron شهري فقط:
#   # في 1 من كل شهر، الساعة 2 فجراً (توقيت الكويت)
#   0 2 1 * * /path/to/run_scraper.sh
#
# الاستخدام مخصص للأغراض الشخصية/الاستشارية. ممنوع النشر التجاري.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$SCRIPT_DIR/log.txt"

echo "=============================" >> "$LOG_FILE"
echo "بدء التحديث الشهري: $(date)" >> "$LOG_FILE"

cd "$SCRIPT_DIR"

# جلب المنتجات (يُرفض تلقائياً إذا تجاوزنا الحد الشهري)
python3 scraper.py >> "$LOG_FILE" 2>&1
SCRAPER_EXIT=$?

if [ $SCRAPER_EXIT -ne 0 ]; then
    echo "خطأ في السكريبر (exit code: $SCRAPER_EXIT)" >> "$LOG_FILE"
fi

# عميل المطابقة
python3 matcher.py >> "$LOG_FILE" 2>&1
MATCHER_EXIT=$?

if [ $MATCHER_EXIT -ne 0 ]; then
    echo "خطأ في عميل المطابقة (exit code: $MATCHER_EXIT)" >> "$LOG_FILE"
fi

# عميل الذكاء الاصطناعي (اختياري — يحتاج ANTHROPIC_API_KEY)
python3 ai_agent.py >> "$LOG_FILE" 2>&1
AI_EXIT=$?

if [ $AI_EXIT -ne 0 ]; then
    echo "خطأ في عميل الذكاء الاصطناعي (exit code: $AI_EXIT)" >> "$LOG_FILE"
fi

echo "انتهى التحديث الشهري: $(date)" >> "$LOG_FILE"
echo "=============================" >> "$LOG_FILE"
