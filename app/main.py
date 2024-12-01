from PyQt6.QtWidgets import QApplication
from app.ui.main_window import MainWindow
import sys
import os

from app.database.database import DB_PATH
from app.utils.database_initializer import database_initializer


def main():
    app = QApplication(sys.argv)
    # Проверка базы данных
    if not os.path.exists(DB_PATH):
        database_initializer()
    # Создание окна и запуск его
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
