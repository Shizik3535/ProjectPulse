from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class EmployeeDetailsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        title = QLabel("Сотрудник ФИО")
        layout.addWidget(title)

        info_label = QLabel("Информация о сотруднике...")
        layout.addWidget(info_label)

        self.btn_add_project = QPushButton("Добавить проект")
        layout.addWidget(self.btn_add_project)

        self.setLayout(layout)
