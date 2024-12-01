from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QFrame
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, pyqtSignal, QSize

from app.resources import ICON_PATH


class Sidebar(QWidget):
    # Сигналы для каждой кнопки
    navigate = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        # Создание виджета для фона
        self.background_widget = QWidget(self)
        self.background_widget.setObjectName("background_widget")

        # Установка фиксированной ширины для бокового меню
        self.setFixedWidth(240)

        # Создаем layout для бокового меню и применяем его
        layout = QVBoxLayout(self.background_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Устанавливаем стиль фона для всего бокового меню
        self.setStyleSheet("""
            #background_widget {
                background: rgba(0, 0, 0, 0.5);
                border-radius: 20px;
            }
            QLabel {
                color: white;
                margin-left: 5px;
                font-size: 24px;
                font-weight: bold;
            }
            QPushButton {
                text-align: left;
                font-size: 16px;
                color: white;
                background: transparent;
                border: none;
                padding: 5px 10px;
                border-radius: 20px;
                margin: 0px 10px;
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 0.2);
            }
        """)

        # Инициализация интерфейса
        self.init_ui(layout)

    def init_ui(self, layout):
        # Создание верхней панели с логотипом и названием
        logo_layout = QHBoxLayout()
        logo_label = QLabel("ProjectPulse")
        logo_layout.addWidget(logo_label)
        layout.addLayout(logo_layout)
        layout.addSpacing(10)

        # Создание кнопок с иконками и подключение их к сигналам
        self.btn_home = self.create_button("Главная", ICON_PATH["home"])
        self.btn_projects = self.create_button("Проекты", ICON_PATH["projects"])
        self.btn_tasks = self.create_button("Задачи", ICON_PATH["tasks"])
        self.btn_employees = self.create_button("Сотрудники", ICON_PATH["employees"])
        self.btn_reports = self.create_button("Отчёты", ICON_PATH["reports"])
        self.btn_settings = self.create_button("Настройки", ICON_PATH["settings"])

        # Добавление кнопок в layout
        layout.addWidget(self.btn_home)
        layout.addWidget(self.btn_projects)
        layout.addWidget(self.btn_tasks)
        layout.addWidget(self.btn_employees)
        layout.addWidget(self.btn_reports)
        layout.addStretch()
        layout.addWidget(self.btn_settings)

        # Устанавливаем layout для виджета
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.background_widget)

    def create_button(self, text, icon_path):
        button = QPushButton(text)

        # Устанавливаем иконку для кнопки
        button.setIcon(QIcon(icon_path))

        # Устанавливаем размер иконки
        button.setIconSize(QSize(40, 40))

        # Подключаем сигнал на нажатие кнопки
        button.clicked.connect(lambda: self.navigate.emit(text.lower()))

        return button
