from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class ReportsPage(QWidget):
    def __init__(self):
        super().__init__()

        # Настроим layout
        layout = QVBoxLayout(self)

        # Заголовок страницы
        title = QLabel("Страница отчётов", self)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        # Устанавливаем layout для виджета
        self.setLayout(layout)