from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QStackedWidget, QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt
from app.ui.components.sidebar import Sidebar
from app.ui.components.statusbar import StatusBar
from app.ui.pages.staff_page import StaffPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ProjectPulse")
        self.resize(1024, 720)
        self.setMinimumSize(1024, 720)

        # Установка градиента фона
        self.setStyleSheet(""" 
            MainWindow { 
                background: qlineargradient(
                    spread: pad, 
                    x1: 0, y1: 0, x2: 1, y2: 1, 
                    stop: 0 #1c282e, stop: 1 #273e4b 
                ); 
            } 

            QStackedWidget { 
                background: #000; 
            } 
        """)

        # История навигации
        self.navigation_history = [{'page': 0}]  # Начальный элемент: Главная страница
        self.current_index = 0

        # Основной виджет и макеты
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QHBoxLayout()
        self.sidebar = Sidebar()
        main_layout.addWidget(self.sidebar)

        content_widget = QWidget()
        content_layout = QVBoxLayout()

        # Инициализация статус-бара
        self.status_bar = StatusBar()
        content_layout.addWidget(self.status_bar)

        self.stack = QStackedWidget()
        content_layout.addWidget(self.stack)
        content_widget.setLayout(content_layout)
        main_layout.addWidget(content_widget)

        # Страницы создаются только по мере необходимости
        self.pages = {
            "главная": None,
            "проекты": None,
            "проект": None,
            "задачи": None,
            "задача": None,
            "сотрудники": None,
            "сотрудник": None,
            "отчёты": None,
            "настройки": None,
        }

        # Обработка сигналов
        self.sidebar.navigate.connect(self.switch_page)
        self.status_bar.back_signal.connect(self.go_back)
        self.status_bar.forward_signal.connect(self.go_forward)
        self.status_bar.reload_signal.connect(self.reload_page)

        main_widget.setLayout(main_layout)

    def create_page(self, page_name, **kwargs):
        """Функция для создания страницы при первом переходе."""
        if page_name == "главная":
            return self.create_placeholder_page("Главная")
        elif page_name == "проекты":
            return self.create_projects_page()
        elif page_name == "проект":
            return self.create_placeholder_page("Проект", project_id=kwargs.get('project_id'))
        elif page_name == "задачи":
            return self.create_tasks_page()
        elif page_name == "задача":
            return self.create_placeholder_page("Задача", task_id=kwargs.get('task_id'))
        elif page_name == "сотрудники":
            return StaffPage()  # Страница сотрудников
        elif page_name == "сотрудник":
            return self.create_placeholder_page("Сотрудник", staff_id=kwargs.get('staff_id'))
        elif page_name == "отчёты":
            return self.create_placeholder_page("Отчёты")
        elif page_name == "настройки":
            return self.create_placeholder_page("Настройки")

    def create_placeholder_page(self, title, **kwargs):
        page = QWidget()
        layout = QVBoxLayout()
        label = QLabel(f"{title}")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px; color: white;")
        layout.addWidget(label)

        # Показ id, если передан
        for key, value in kwargs.items():
            if value is not None:
                id_label = QLabel(f"{key.capitalize()} ID: {value}")
                id_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                id_label.setStyleSheet("font-size: 18px; color: white;")
                layout.addWidget(id_label)

        page.setLayout(layout)
        return page

    def create_projects_page(self):
        page = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Страница проектов")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px; color: white;")
        layout.addWidget(label)

        # Кнопки для переключения на детализированные страницы проекта
        button1 = QPushButton("Детали проекта 1")
        button1.clicked.connect(lambda: self.switch_page("проект", project_id=1))
        layout.addWidget(button1)

        button2 = QPushButton("Детали проекта 2")
        button2.clicked.connect(lambda: self.switch_page("проект", project_id=2))
        layout.addWidget(button2)

        page.setLayout(layout)
        return page

    def create_tasks_page(self):
        page = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Страница задач")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px; color: white;")
        layout.addWidget(label)

        # Кнопки для переключения на детализированные страницы задачи
        button1 = QPushButton("Детали задачи 1")
        button1.clicked.connect(lambda: self.switch_page("задача", task_id=1))
        layout.addWidget(button1)

        button2 = QPushButton("Детали задачи 2")
        button2.clicked.connect(lambda: self.switch_page("задача", task_id=2))
        layout.addWidget(button2)

        page.setLayout(layout)
        return page

    def update_navigation_buttons(self):
        # Скрываем/показываем кнопку "назад"
        self.status_bar.back_button.setVisible(self.current_index > 0)
        # Скрываем/показываем кнопку "вперёд"
        self.status_bar.forward_button.setVisible(self.current_index < len(self.navigation_history) - 1)

    def switch_page(self, page_name, **kwargs):
        try:
            # Если страница еще не создана, создаем её
            if self.pages[page_name] is None:
                self.pages[page_name] = self.create_page(page_name, **kwargs)
                self.stack.addWidget(self.pages[page_name])

            # Переключаемся на нужную страницу
            index = list(self.pages.keys()).index(page_name)
            page_data = {'page': index}

            # Добавляем параметры в словарь page_data
            for key, value in kwargs.items():
                page_data[key] = value

            # Обрезка истории, если переходим на новую страницу после возврата
            if self.current_index < len(self.navigation_history) - 1:
                self.navigation_history = self.navigation_history[:self.current_index + 1]

            # Добавление новой страницы в историю
            self.navigation_history.append(page_data)
            self.current_index += 1

            self.stack.setCurrentIndex(index)
            self.status_bar.update_title(page_name.capitalize())

            # Обновление кнопок навигации
            self.update_navigation_buttons()

        except Exception as e:
            print(f"Error switching page: {e}")

    def go_back(self):
        if self.current_index > 0:
            self.current_index -= 1
            current_page = self.navigation_history[self.current_index]
            self.stack.setCurrentIndex(current_page['page'])
            self.update_status_title()
            self.update_navigation_buttons()

    def go_forward(self):
        if self.current_index < len(self.navigation_history) - 1:
            self.current_index += 1
            current_page = self.navigation_history[self.current_index]
            self.stack.setCurrentIndex(current_page['page'])
            self.update_status_title()
            self.update_navigation_buttons()

    def reload_page(self):
        current_page_index = self.stack.currentIndex()
        # Логика обновления текущей страницы (пока пустая)

    def update_status_title(self):
        current_page = self.navigation_history[self.current_index]
        current_page_name = list(self.pages.keys())[current_page['page']]
        self.status_bar.update_title(current_page_name.capitalize())
