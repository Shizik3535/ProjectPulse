from sqlalchemy import insert, select, update, delete

from app.database.database import session_maker


class BaseDAO:
    """Базовый DAO, в котором есть CRUD операции"""
    model = None

    # Чтение
    @classmethod
    def find_all(cls, **filters):
        """Найти все записи в таблице"""
        with session_maker() as session:
            query = select(cls.model).filter_by(**filters)
            result = session.execute(query)
            return result.scalars().all()

    @classmethod
    def find_one_or_none(cls, **filters):
        """Поиск одной записи по фильтру"""
        with session_maker() as session:
            query = select(cls.model).filter_by(**filters)
            result = session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    def find_by_id(cls, model_id: int):
        """Поиск одной записи по id"""
        with session_maker() as session:
            query = select(cls.model).where(cls.model.id == model_id)
            result = session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    def create(cls, **data):
        """Создание записи"""
        with session_maker() as session:
            query = insert(cls.model).values(**data)
            session.execute(query)
            session.commit()

    @classmethod
    def create_many(cls, *data):
        """Создание нескольких записей"""
        with session_maker() as session:
            query = insert(cls.model).values(*data)
            session.execute(query)
            session.commit()

    @classmethod
    def update(cls, model_id: int, **data):
        """Обновление записи по id"""
        with session_maker() as session:
            query = update(cls.model).where(cls.model.id == model_id).values(**data)
            session.execute(query)
            session.commit()

    @classmethod
    def delete(cls, model_id: int):
        """Удаление записи по id"""
        with session_maker() as session:
            query = delete(cls.model).where(cls.model.id == model_id)
            session.execute(query)
            session.commit()

    @classmethod
    def delete_by_filter(cls, **filters):
        """Удаление записей по фильтру"""
        with session_maker() as session:
            query = delete(cls.model).filter_by(**filters)
            session.execute(query)
            session.commit()
