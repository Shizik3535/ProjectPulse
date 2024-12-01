from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database.database import Base


class StatusTask(Base):
    __tablename__ = 'status_tasks'

    # Атрибуты
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    # Связи
    tasks = relationship('Task', back_populates='status')


class Task(Base):
    __tablename__ = 'tasks'

    # Атрибуты
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)

    # Внешние ключи
    project_id = Column(Integer, ForeignKey('projects.id', ondelete="SET NULL"), nullable=True)
    status_id = Column(Integer, ForeignKey('status_tasks.id', ondelete="SET NULL"), nullable=True)

    # Связи
    status = relationship('StatusTask', back_populates='tasks', lazy='joined')
    project = relationship('ProjectTask', back_populates='tasks')
    members = relationship('TaskMember', back_populates='task')


class TaskMember(Base):
    __tablename__ = 'task_members'

    # Атрибуты
    id = Column(Integer, primary_key=True)

    # Внешние ключи
    task_id = Column(Integer, ForeignKey('tasks.id', ondelete="CASCADE"), nullable=False)
    staff_id = Column(Integer, ForeignKey('staff.id', ondelete="CASCADE"), nullable=False)

    # Связи
    staff = relationship("Staff", back_populates="tasks")
    task = relationship("Task", back_populates="members")
