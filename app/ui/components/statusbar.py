from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt, QSize, pyqtSignal
from PyQt6.QtGui import QIcon

from app.resources import ICON_PATH


class StatusBar(QWidget):
    # Определяем сигналы для кнопок
    back_signal = pyqtSignal()
    forward_signal = pyqtSignal()
    reload_signal = pyqtSignal()
    update_title_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # Основной layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Фоновый виджет
        self.background_widget = QWidget(self)
        self.background_widget.setObjectName("background_widget")

        # Создаем горизонтальный layout для элементов статус-бара
        layout = QHBoxLayout(self.background_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Устанавливаем стиль для фонового виджета
        self.setStyleSheet("""
            #background_widget {
                background: rgba(0, 0, 0, 0.5);
                border-radius: 20px;
                padding: 10px;
            }
            QPushButton {
                color: white;
                background: transparent;
                border: none;
                padding: 5px 10px;
                border-radius: 5px;
                margin-right: 10px;
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 0.2);
            }
            QLabel {
                color: white;
                font-size: 18px;
                font-weight: bold;
                margin-left: 20px;
            }
        """)

        # Инициализация интерфейса
        self.init_ui(layout)

        # Добавляем фоновый виджет в основной layout
        main_layout.addWidget(self.background_widget)

        # Подключаем сигнал обновления заголовка к слоту
        self.update_title_signal.connect(self.update_title)

    def init_ui(self, layout):
        # Название текущей страницы
        self.page_title = QLabel("Главная")
        layout.addWidget(self.page_title)
        layout.addStretch()

        # Кнопки навигации
        self.back_button = QPushButton()
        self.back_button.setIcon(QIcon(ICON_PATH['left']))
        self.back_button.setIconSize(QSize(25, 25))
        self.back_button.clicked.connect(self.back_signal.emit)
        self.back_button.setVisible(False)

        self.forward_button = QPushButton()
        self.forward_button.setIcon(QIcon(ICON_PATH['right']))
        self.forward_button.setIconSize(QSize(25, 25))
        self.forward_button.clicked.connect(self.forward_signal.emit)
        self.forward_button.setVisible(False)

        self.reload_button = QPushButton()
        self.reload_button.setIcon(QIcon(ICON_PATH['refresh']))
        self.reload_button.setIconSize(QSize(25, 25))
        self.reload_button.clicked.connect(self.reload_signal.emit)

        layout.addWidget(self.back_button)
        layout.addWidget(self.forward_button)
        layout.addWidget(self.reload_button)

    def update_title(self, new_title):
        self.page_title.setText(new_title)
