from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QDateEdit, QPushButton, QLabel, QComboBox, QErrorMessage
from PyQt6.QtCore import QDate

from datetime import datetime

from app.database.dao.projects import ProjectDAO, StatusProjectDAO
from app.database.models import Project, StatusProject


class ProjectForm(QDialog):
    def __init__(self, parent=None, project=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить проект" if not project else "Редактировать проект")
        self.setFixedSize(400, 300)
        self.project = project  # Сохраняем проект, если передан
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Название проекта
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Название проекта")
        if self.project:
            self.name_input.setText(self.project.name)
        layout.addWidget(self.name_input)

        # Описание проекта
        self.description_input = QLineEdit(self)
        self.description_input.setPlaceholderText("Описание проекта")
        if self.project:
            self.description_input.setText(self.project.description)
        layout.addWidget(self.description_input)

        # Дата начала
        self.start_date_input = QDateEdit(self)
        if self.project:
            self.start_date_input.setDate(QDate.fromString(self.project.start_date, "yyyy-MM-dd"))
        else:
            self.start_date_input.setDate(QDate.currentDate())
        layout.addWidget(self.start_date_input)

        # Дата окончания
        self.end_date_input = QDateEdit(self)
        if self.project:
            self.end_date_input.setDate(QDate.fromString(self.project.end_date, "yyyy-MM-dd"))
        else:
            self.end_date_input.setDate(QDate.currentDate())
        layout.addWidget(self.end_date_input)

        # Статус проекта (загрузка данных из базы через StatusProjectDAO)
        self.status_input = QComboBox(self)
        self.load_statuses()  # Загружаем статусы
        if self.project and self.project.status:
            # Устанавливаем текст статуса, если проект редактируется
            self.status_input.setCurrentText(self.project.status.name)
        layout.addWidget(self.status_input)

        # Кнопка "Сохранить"
        self.save_button = QPushButton("Сохранить", self)
        self.save_button.clicked.connect(self.save_project)
        layout.addWidget(self.save_button)

        # Кнопка "Отмена"
        self.cancel_button = QPushButton("Отмена", self)
        self.cancel_button.clicked.connect(self.reject)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

    def load_statuses(self):
        # Загружаем все статусы из базы данных через StatusProjectDAO
        statuses = StatusProjectDAO.find_all()
        self.status_input.clear()  # Очищаем текущий список

        # Добавляем пункт "Ничего" в выпадающий список
        self.status_input.addItem("Ничего", None)

        # Заполняем выпадающий список статусами
        for status in statuses:
            # Добавляем текст статуса и сохраняем его ID в качестве данных
            self.status_input.addItem(status.name, status.id)

    def save_project(self):
        # Получаем значения из полей ввода
        name = self.name_input.text()
        description = self.description_input.text()
        start_date = self.start_date_input.date().toString("yyyy-MM-dd")
        end_date = self.end_date_input.date().toString("yyyy-MM-dd")
        status_id = self.status_input.currentData()  # Получаем выбранный ID статуса

        # Если выбран статус, получаем его ID
        status = None
        if status_id:
            status = status_id  # Сохраняем только ID статуса

        if not name:
            error_message = QErrorMessage(self)
            error_message.setWindowTitle("Ошибка")  # Установка заголовка окна
            error_message.showMessage("Произошла ошибка! Заполните введите название проекта.")
            error_message.exec()
            return
        if self.project:
            # Обновление существующего проекта
            ProjectDAO.update(
                model_id=self.project.id,
                name=name,
                description=description,
                start_date=start_date,
                end_date=end_date,
                status=status
            )
        else:
            # Создание нового проекта
            print("Project create")
            ProjectDAO.create(
                name=name,
                description=description,
                start_date=start_date,
                end_date=end_date,
                status_id=status
            )
        print(f"Проект сохранён: {name}, {description}, {start_date}, {end_date}, {status_id}")

        self.accept()  # Закрытие формы после сохранения
