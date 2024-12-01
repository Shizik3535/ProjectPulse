from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem,
    QHeaderView, QHBoxLayout, QLabel, QDialog
)
from PyQt6.QtCore import Qt

from app.ui.forms.project_form import ProjectForm

from app.database.dao.projects import ProjectDAO


class ProjectsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setStyleSheet(""" 
        QPushButton {
            background: rgba(0, 0, 0, 0.5);
            color: #fff;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 20px;
        }
        QPushButton:hover {
            background-color: #555;
        }
        QLineEdit {
            background: rgba(0, 0, 0, 0.5);
            border: none;
            padding: 10px;
            font-size: 16px;
            border-radius: 20px;
            color: #fff;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
        }
        """)

    def init_ui(self):
        # Основной layout страницы
        layout = QVBoxLayout(self)

        # Верхняя панель с кнопкой и строкой поиска
        top_bar = QHBoxLayout()

        # Строка поиска
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Поиск проектов...")
        self.search_input.textChanged.connect(self.filter_projects)
        top_bar.addWidget(self.search_input)

        # Кнопка "Добавить проект"
        self.add_button = QPushButton("Добавить проект")
        self.add_button.clicked.connect(self.open_add_project_form)
        top_bar.addWidget(self.add_button)

        layout.addLayout(top_bar)
        layout.addSpacing(10)

        # Создание таблицы для проектов
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Название проекта", "Описание", "Дата начала", "Дата конца", "Статус"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Отключаем нумерацию строк
        self.table.verticalHeader().setVisible(False)

        # Включаем выделение всей строки
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        # Обработка двойного нажатия
        self.table.cellDoubleClicked.connect(self.on_cell_double_clicked)

        # Метка для отображения сообщения о пустых данных
        self.no_projects_label = QLabel("Нет проектов")
        self.no_projects_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.no_projects_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                color: #fff;
                background: rgba(0, 0, 0, 0.5);
                border-radius: 20px;
                padding: 10px;
            }
        """)

        # Популяция таблицы
        self.populate_table()

        # Стилизация таблицы
        self.style_table()

        layout.addWidget(self.table)
        layout.addWidget(self.no_projects_label)  # Добавляем метку в layout
        self.setLayout(layout)

    def populate_table(self):
        # Пример данных, позже можно заменить на данные из БД
        projects = [
            (
                project.id,
                project.name,
                project.description if project.description else "",
                project.start_date if project.start_date else "",
                project.end_date if project.end_date else "",
                project.status.name if project.status else "",
            )
            for project in ProjectDAO.find_all()
        ]

        if not projects:  # Если проектов нет, показываем метку
            self.table.setVisible(False)
            self.no_projects_label.setVisible(True)
        else:
            self.table.setRowCount(len(projects))
            for row, project in enumerate(projects):
                for col, value in enumerate(project):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # Запрет редактирования
                    self.table.setItem(row, col, item)

            self.table.setVisible(True)
            self.no_projects_label.setVisible(False)

    def open_add_project_form(self):
        # Открытие формы добавления проекта
        add_project_form = ProjectForm(self)
        if add_project_form.exec() == QDialog.DialogCode.Accepted:
            # Если проект добавлен, обновляем таблицу
            self.populate_table()


    def filter_projects(self):
        # Фильтрация таблицы по строке поиска
        search_text = self.search_input.text().lower()
        for row in range(self.table.rowCount()):
            match = False
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item and search_text in item.text().lower():
                    match = True
            self.table.setRowHidden(row, not match)

    def on_cell_double_clicked(self, row, column):
        # Получаем ID проекта из скрытой первой колонки и выводим его в консоль
        project_id = self.table.item(row, 0).text()
        print(f"Двойное нажатие по ID: {project_id}")

    def style_table(self):
        # Стилизация таблицы через QSS
        self.table.setStyleSheet("""
            QTableWidget {
                background: rgba(0, 0, 0, 0.5);
                gridline-color: #cccccc;
                font-size: 14px;
                border-radius: 20px;
            }
            QHeaderView::section {
                background: rgba(0, 0, 0, 0.1);
                color: white;
                font-weight: bold;
                padding: 5px;
                border: 0.5px solid #fff;
            }
            QTableWidget QTableCornerButton::section {
                background: rgba(0, 0, 0, 0.3);
            }
            QTableWidget::item {
                padding: 10px;
            }
            QTableWidget::item:selected {
                background: rgba(100, 100, 100, 0.5);
            }
        """)
