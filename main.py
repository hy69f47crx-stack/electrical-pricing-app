#!/usr/bin/env python3
"""
نقطة الدخول الرئيسية لتطبيق تصنيف الملفات
"""

import sys
import logging
from pathlib import Path
from PyQt6.QtWidgets import QApplication
from app.ui.login_window import LoginWindow
from app.ui.main_window import MainWindow
import config

# إعداد التسجيل
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(config.LOGS_DIR / "app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def main():
    """البرنامج الرئيسي"""
    app = QApplication(sys.argv)

    # تعيين أسلوب التطبيق
    app.setStyle('Fusion')

    # عرض نافذة الدخول
    login_window = LoginWindow()
    login_window.show()

    def on_login_success(password):
        """معالج النجاح في تسجيل الدخول"""
        login_window.close()
        main_window = MainWindow(password)
        main_window.show()
        logger.info("تم فتح النافذة الرئيسية بنجاح")

    login_window.login_success.connect(on_login_success)

    logger.info("تم بدء التطبيق بنجاح")
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
