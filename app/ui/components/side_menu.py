from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, Qt, pyqtSignal
from app.resources import ICON_PATH


class SideMenu(QWidget):
    # Сигналы для каждой кнопки
    home_clicked = pyqtSignal()
    projects_clicked = pyqtSignal()
    tasks_clicked = pyqtSignal()
    employees_clicked = pyqtSignal()
    reports_clicked = pyqtSignal()
    settings_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setFixedWidth(250)  # Устанавливаем фиксированную ширину меню

        # Внутренний виджет для стилизации
        self.inner_widget = QWidget(self)
        self.inner_widget.setObjectName("innerWidget")
        self.inner_widget.setStyleSheet("""
            #innerWidget {
                background-color: rgba(0, 0, 0, 0.5);
                border-radius: 20px;
                padding: 10px;
            }
            QPushButton {
                background-color: transparent;
                color: #fff;
                border: none;
                padding: 10px 20px;
                border-radius: 10px;
                text-align: left;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #555;
                border-radius: 10px;
            }
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: white;
                padding: 10px 20px;
            }
        """)

        # Создание layout для бокового меню
        layout = QVBoxLayout(self.inner_widget)

        # Название приложения
        app_title = QLabel("ProjectPulse", self)
        app_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(app_title)

        # Кнопки для навигации
        self.create_menu_button("Главная", ICON_PATH['home'], self.home_clicked)
        self.create_menu_button("Проекты", ICON_PATH['projects'], self.projects_clicked)
        self.create_menu_button("Задачи", ICON_PATH['tasks'], self.tasks_clicked)
        self.create_menu_button("Сотрудники", ICON_PATH['employees'], self.employees_clicked)
        self.create_menu_button("Отчёты", ICON_PATH['reports'], self.reports_clicked)
        layout.addStretch()  # Пропуск расстояния до низа
        self.create_menu_button("Настройки", ICON_PATH['settings'], self.settings_clicked)

        # Устанавливаем layout для внутреннего виджета
        self.inner_widget.setLayout(layout)

        # Устанавливаем layout для основного виджета
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.inner_widget)
        self.setLayout(main_layout)

    def create_menu_button(self, text, icon_path, signal):
        """Метод для создания кнопки с иконкой и текстом, а также подключения сигнала"""
        button = QPushButton(text, self)
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(24, 24))
        button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #fff;
                border: none;
                padding: 10px 20px;
                border-radius: 10px;
                text-align: left;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #555;
                border-radius: 10px;
            }
        """)
        # Подключение сигнала кнопки
        button.clicked.connect(signal)
        # Добавление кнопки в layout
        self.inner_widget.layout().addWidget(button)
