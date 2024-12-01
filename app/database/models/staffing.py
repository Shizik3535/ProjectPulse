from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base


class Position(Base):
    __tablename__ = 'positions'

    # Атрибуты
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    # Связи
    staff = relationship('Staff', back_populates='position')


class Staff(Base):
    __tablename__ = 'staff'

    # Атрибуты
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    patronymic = Column(String, nullable=True)

    # Внешние ключи
    position_id = Column(Integer, ForeignKey('positions.id', ondelete="SET NULL"), nullable=True)

    # Связи
    position = relationship('Position', back_populates='staff', lazy='joined')
    projects = relationship('ProjectMember', back_populates='staff')
    tasks = relationship('TaskMember', back_populates='staff')
