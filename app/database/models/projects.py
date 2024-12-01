from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database.database import Base


class StatusProject(Base):
    __tablename__ = 'status_projects'

    # Атрибуты
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    # Связи
    projects = relationship('Project', back_populates='status')


class Project(Base):
    __tablename__ = 'projects'

    # Атрибуты
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    # Внешние ключи
    status_id = Column(Integer, ForeignKey('status_projects.id', ondelete="SET NULL"), nullable=True)

    # Связи
    status = relationship('StatusProject', back_populates='projects', lazy='joined')
    tasks = relationship('ProjectTask', back_populates='project', cascade="all, delete-orphan")
    members = relationship('ProjectMember', back_populates='project', cascade="all, delete-orphan")


class ProjectMember(Base):
    __tablename__ = 'project_members'

    # Атрибуты
    id = Column(Integer, primary_key=True)

    # Внешние ключи
    staff_id = Column(Integer, ForeignKey('staff.id', ondelete="CASCADE"), nullable=False)
    project_id = Column(Integer, ForeignKey('projects.id', ondelete="CASCADE"), nullable=False)

    # Связи
    staff = relationship('Staff', back_populates='projects')
    project = relationship('Project', back_populates='members')


class ProjectTask(Base):
    __tablename__ = 'project_tasks'

    # Атрибуты
    id = Column(Integer, primary_key=True)

    # Внешние ключи
    project_id = Column(Integer, ForeignKey('projects.id', ondelete="CASCADE"), nullable=False)
    task_id = Column(Integer, ForeignKey('tasks.id', ondelete="CASCADE"), nullable=False)

    # Связи
    project = relationship('Project', back_populates='tasks')
    tasks = relationship('Task', back_populates='project')
