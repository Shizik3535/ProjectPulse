from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget

from app.ui.components.status_bar import StatusBar
from app.ui.components.side_menu import SideMenu
from app.ui.pages.home_page import HomePage
from app.ui.pages.projects_page import ProjectsPage
from app.ui.pages.tasks_page import TasksPage
from app.ui.pages.employees_page import EmployeesPage
from app.ui.pages.reports_page import ReportsPage
from app.ui.pages.settings_page import SettingsPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройки окна
        self.setWindowTitle("ProjectPulse")
        self.resize(1024, 720)
        self.setMinimumSize(1024, 720)
        self.setStyleSheet(""" 
            MainWindow { 
                background: qlineargradient(
                    spread: pad, 
                    x1: 0, y1: 0, x2: 1, y2: 1, 
                    stop: 0 #1c282e, stop: 1 #273e4b 
                );
            }
        """)

        # Словарь страниц: ключ — индекс, значение — кортеж (класс страницы, заголовок)
        self.page_classes = {
            0: (HomePage, "Главная"),
            1: (ProjectsPage, "Проекты"),
            2: (TasksPage, "Задачи"),
            3: (EmployeesPage, "Сотрудники"),
            4: (ReportsPage, "Отчёты"),
            5: (SettingsPage, "Настройки")
        }

        # Инициализация UI
        self.init_ui()

    def init_ui(self):
        # Главный виджет
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Создание основного контента
        content_widget = QWidget(self)

        # Основной контент
        self.stacked_widget = QStackedWidget(self)
        self.page_instances = {}  # Храним созданные экземпляры страниц

        # Создание бокового меню
        self.side_menu = SideMenu()
        self.side_menu.home_clicked.connect(lambda: self.show_page(0))
        self.side_menu.projects_clicked.connect(lambda: self.show_page(1))
        self.side_menu.tasks_clicked.connect(lambda: self.show_page(2))
        self.side_menu.employees_clicked.connect(lambda: self.show_page(3))
        self.side_menu.reports_clicked.connect(lambda: self.show_page(4))
        self.side_menu.settings_clicked.connect(lambda: self.show_page(5))

        # Создание строки состояния
        self.status_bar = StatusBar()
        self.status_bar.back_clicked.connect(self.go_back)
        self.status_bar.forward_clicked.connect(self.go_forward)
        self.status_bar.reload_clicked.connect(self.reload_content)

        # Создание layouts
        main_layout = QHBoxLayout(main_widget)
        content_layout = QVBoxLayout()

        # Установка layouts для основного контента
        content_widget.setLayout(content_layout)

        # Добавление в layouts бокового меню, строки состояния и основного контента
        content_layout.addWidget(self.status_bar)
        content_layout.addWidget(self.stacked_widget)
        main_layout.addWidget(self.side_menu)
        main_layout.addWidget(content_widget)

        # Показать главную страницу по умолчанию
        self.show_page(0)

    def show_page(self, index):
        """Показать страницу по индексу, создавая её при необходимости"""
        if index not in self.page_instances:
            # Создаем экземпляр страницы и добавляем его в QStackedWidget
            page_class, title = self.page_classes[index]
            page_instance = page_class()
            self.page_instances[index] = page_instance
            self.stacked_widget.addWidget(page_instance)

        # Устанавливаем текущую страницу
        self.stacked_widget.setCurrentWidget(self.page_instances[index])
        # Устанавливаем заголовок в строке состояния
        self.set_section_title(self.page_classes[index][1])

    def set_section_title(self, title):
        """Изменение заголовка в строке состояния"""
        self.status_bar.set_section_title(title)

    def go_back(self):
        print("Кнопка 'Назад' нажата")

    def go_forward(self):
        print("Кнопка 'Вперёд' нажата")

    def reload_content(self):
        print("Кнопка 'Перезагрузить' нажата")
