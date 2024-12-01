from app.database.dao.base import BaseDAO

from app.database.models.projects import Project, ProjectTask, ProjectMember, StatusProject


class ProjectDAO(BaseDAO):
    model = Project


class StatusProjectDAO(BaseDAO):
    model = StatusProject


class ProjectMemberDAO(BaseDAO):
    model = ProjectMember


class ProjectTaskDAO(BaseDAO):
    model = ProjectTask
