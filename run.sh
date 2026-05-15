#!/bin/bash

# تفعيل Virtual Environment وتشغيل التطبيق

cd "$(dirname "$0")"

# التحقق من وجود venv
if [ ! -d "venv" ]; then
    echo "📦 إنشاء بيئة افتراضية..."
    python3 -m venv venv
fi

# تفعيل البيئة
echo "🚀 تفعيل البيئة الافتراضية..."
source venv/bin/activate

# تشغيل التطبيق
echo "▶️  تشغيل التطبيق..."
python main.py
