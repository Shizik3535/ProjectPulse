from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
import os


# URL Базы данных
base_dir = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(base_dir, '../../', 'projectpulse.db')
DB_URL = f'sqlite:///{os.path.abspath(DB_PATH)}'


# Создание движка
engine = create_engine(DB_URL, echo=True)

# Создание функции для взятия сессий
session_maker = sessionmaker(
    bind=engine,
    class_=Session,
    expire_on_commit=False
)


# Класс для работы с базой данных
class Base(DeclarativeBase):
    pass
