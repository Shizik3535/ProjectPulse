from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton
from app.database.dao.staffing import StaffDAO


class StaffPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Сотрудники")
        self.setStyleSheet("background-color: #273e4b; color: white;")

        # Инициализация макета
        layout = QVBoxLayout()

        # Таблица для отображения сотрудников
        self.table = QTableWidget()
        self.table.setColumnCount(5)  # 5 колонок: ID, Имя, Фамилия, Отчество, Должность
        self.table.setHorizontalHeaderLabels(["ID", "Имя", "Фамилия", "Отчество", "Должность"])
        layout.addWidget(self.table)

        # Кнопка для добавления нового сотрудника (по желанию)
        self.add_button = QPushButton("Добавить сотрудника")
        layout.addWidget(self.add_button)

        # Загружаем данные сотрудников
        self.load_staff_data()

        self.setLayout(layout)

    def load_staff_data(self):
        """Загружаем данные сотрудников и заполняем таблицу"""
        staff_list = StaffDAO.find_all()  # Получаем всех сотрудников через DAO

        # Очищаем таблицу перед добавлением данных
        self.table.setRowCount(0)

        # Заполняем таблицу данными
        for staff in staff_list:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)

            # Заполняем ячейки данными сотрудника
            self.table.setItem(row_position, 0, QTableWidgetItem(str(staff.id)))
            self.table.setItem(row_position, 1, QTableWidgetItem(staff.first_name))
            self.table.setItem(row_position, 2, QTableWidgetItem(staff.last_name))
            self.table.setItem(row_position, 3, QTableWidgetItem(staff.patronymic or ""))
            self.table.setItem(row_position, 4, QTableWidgetItem(staff.position.name if staff.position else "Не указано"))
