from alembic import command
from alembic.config import Config
import os

from app.database.database import DB_PATH
from app.database.dao import StatusTaskDAO, StatusProjectDAO, PositionDAO


def database_initializer():
    def initialize_db():
        with open(DB_PATH, 'w'):
            pass

    def run_migrations():
        config_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../alembic.ini'))
        config = Config(config_path)
        config.set_main_option('script_location', os.path.abspath(os.path.join(os.path.dirname(config_path), 'migrations')))
        command.upgrade(config, "head")

    def insert_base_data():
        # Статусы проектов
        StatusProjectDAO.create_many(
            [
                {"name": "Запланирован"},
                {"name": "В процессе"},
                {"name": "Завершен"},
                {"name": "На паузе"},
                {"name": "Отменен"},
            ]
        )

        # Статусы задач
        StatusTaskDAO.create_many(
            [
                {"name": "Новая"},
                {"name": "В работе"},
                {"name": "Завершена"},
                {"name": "Отменена"},
                {"name": "Отложена"},
                {"name": "Перенесена"},
            ]
        )

        # Должности
        PositionDAO.create_many(
            [
                {"name": "Руководитель"},
                {"name": "Менеджер"},
                {"name": "Стажер"},
                {"name": "Инженер"},
                {"name": "Специалист"},
                {"name": "Администратор"},
                {"name": "Системный администратор"},
                {"name": "Маркетолог"},
                {"name": "Бухгалтер"},
                {"name": "Преподаватель"},
                {"name": "HR-менеджер"},
                {"name": "Продажник"},
                {"name": "Аналитик"},
                {"name": "Техподдержка"},
                {"name": "Креативный директор"},
                {"name": "Юрист"},
                {"name": "Офис-менеджер"},
                {"name": "Менеджер по работе с клиентами"},
            ]
        )

    initialize_db()
    run_migrations()
    insert_base_data()
