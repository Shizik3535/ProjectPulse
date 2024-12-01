from app.database.dao.base import BaseDAO

from app.database.models.tasks import Task, TaskMember, StatusTask


class TaskDAO(BaseDAO):
    model = Task


class TaskMemberDAO(BaseDAO):
    model = TaskMember


class StatusTaskDAO(BaseDAO):
    model = StatusTask
