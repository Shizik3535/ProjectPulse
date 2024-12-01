from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTableWidget,
    QTableWidgetItem, QHeaderView, QLabel, QDialog
)
from PyQt6.QtCore import Qt
# from app.ui.forms.staff_form import StaffForm  # Если будет форма для добавления сотрудников
from app.database.dao.staffing import StaffDAO


class EmployeesPage(QWidget):
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
        self.search_input.setPlaceholderText("Поиск сотрудников...")
        self.search_input.textChanged.connect(self.filter_staff)
        top_bar.addWidget(self.search_input)

        # Кнопка "Добавить сотрудника"
        self.add_button = QPushButton("Добавить сотрудника")
        self.add_button.clicked.connect(self.open_add_staff_form)
        top_bar.addWidget(self.add_button)

        layout.addLayout(top_bar)
        layout.addSpacing(10)

        # Создание таблицы для сотрудников
        self.table = QTableWidget()
        self.table.setColumnCount(5)  # У нас 5 столбцов для сотрудника
        self.table.setHorizontalHeaderLabels(
            ["ID", "Имя", "Фамилия", "Отчество", "Должность"]
        )
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Отключаем нумерацию строк
        self.table.verticalHeader().setVisible(False)

        # Включаем выделение всей строки
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        # Обработка двойного нажатия
        self.table.cellDoubleClicked.connect(self.on_cell_double_clicked)

        # Метка для отображения сообщения о пустых данных
        self.no_staff_label = QLabel("Нет сотрудников")
        self.no_staff_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.no_staff_label.setStyleSheet("""
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
        layout.addWidget(self.no_staff_label)  # Добавляем метку в layout
        self.setLayout(layout)

    def populate_table(self):
        # Пример данных, позже можно заменить на данные из БД
        staff = [
            (
                employee.id,
                employee.first_name,
                employee.last_name,
                employee.patronymic if employee.patronymic else "",
                employee.position.name if employee.position else "",
            )
            for employee in StaffDAO.find_all()
        ]

        if not staff:  # Если сотрудников нет, показываем метку
            self.table.setVisible(False)
            self.no_staff_label.setVisible(True)
        else:
            self.table.setRowCount(len(staff))
            for row, employee in enumerate(staff):
                for col, value in enumerate(employee):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # Запрет редактирования
                    self.table.setItem(row, col, item)

            self.table.setVisible(True)
            self.no_staff_label.setVisible(False)

    def open_add_staff_form(self):
        # Открытие формы добавления сотрудника
        # add_staff_form = StaffForm(self)
        # if add_staff_form.exec() == QDialog.DialogCode.Accepted:
        #     # Если сотрудник добавлен, обновляем таблицу
        #     self.populate_table()
        pass

    def filter_staff(self):
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
        # Получаем ID сотрудника из скрытой первой колонки и выводим его в консоль
        staff_id = self.table.item(row, 0).text()
        print(f"Двойное нажатие по ID сотрудника: {staff_id}")

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
