from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, pyqtSignal

from app.resources import ICON_PATH


class StatusBar(QWidget):
    # Сигналы для кнопок
    back_clicked = pyqtSignal()
    forward_clicked = pyqtSignal()
    reload_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setFixedHeight(80)

        # Внутренний QWidget для стилизации
        self.inner_widget = QWidget(self)
        self.inner_widget.setObjectName("innerWidget")

        # Стили для внутреннего виджета и кнопок
        self.inner_widget.setStyleSheet("""
        #innerWidget {
            background-color: rgba(0, 0, 0, 0.5);
            border-radius: 20px;
            padding: 10px;
        }
        QLabel {
            font-size: 24px;
            margin-left: 10px;
            font-weight: bold;
        }
        QPushButton {
            background-color: transparent;
            color: #aaa;
            border: none;
            padding: 5px 10px;
            border-radius: 20px;
        }
        QPushButton:hover {
            background-color: #555;
            border-radius: 20px;
        }
        """)

        # Создание layout для строки состояния
        layout = QHBoxLayout(self.inner_widget)

        # Лейбл для отображения текущего раздела
        self.section_label = QLabel("Главная")

        # Кнопки для навигации
        self.back_button = QPushButton()
        self.back_button.setIcon(QIcon(ICON_PATH['left']))
        self.back_button.setIconSize(QSize(30, 30))
        self.forward_button = QPushButton()
        self.forward_button.setIcon(QIcon(ICON_PATH['right']))
        self.forward_button.setIconSize(QSize(30, 30))
        self.reload_button = QPushButton()
        self.reload_button.setIcon(QIcon(ICON_PATH['refresh']))
        self.reload_button.setIconSize(QSize(30, 30))

        # Добавляем элементы в layout
        layout.addWidget(self.section_label)
        layout.addStretch()
        layout.addWidget(self.back_button)
        layout.addWidget(self.forward_button)
        layout.addWidget(self.reload_button)

        # Устанавливаем layout для внутреннего виджета
        self.inner_widget.setLayout(layout)

        # Устанавливаем layout для основного виджета
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.inner_widget)
        self.setLayout(main_layout)

        # Подключение сигналов к методам
        self.back_button.clicked.connect(self.on_back_clicked)
        self.forward_button.clicked.connect(self.on_forward_clicked)
        self.reload_button.clicked.connect(self.on_reload_clicked)

    def set_section_title(self, title):
        """Метод для изменения текста на section_label."""
        self.section_label.setText(title)

    def on_back_clicked(self):
        """Обработчик для кнопки 'Назад'."""
        self.back_clicked.emit()

    def on_forward_clicked(self):
        """Обработчик для кнопки 'Вперёд'."""
        self.forward_clicked.emit()

    def on_reload_clicked(self):
        """Обработчик для кнопки 'Перезагрузить'."""
        self.reload_clicked.emit()
