from app.database.dao.base import BaseDAO

from app.database.models.staffing import Staff, Position


class StaffDAO(BaseDAO):
    model = Staff


class PositionDAO(BaseDAO):
    model = Position
