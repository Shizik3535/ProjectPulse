from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class ProjectDetailsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        title = QLabel("Проект НАЗВАНИЕ")
        layout.addWidget(title)

        info_label = QLabel("Информация о проекте...")
        layout.addWidget(info_label)

        self.btn_create_task = QPushButton("Создать задачу")
        layout.addWidget(self.btn_create_task)

        self.setLayout(layout)
