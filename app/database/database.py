from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
import os


# URL Базы данных
DB_URL = f'postgresql://postgres:postgres@localhost:5432/test_projectpulse'


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
