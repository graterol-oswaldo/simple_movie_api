from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean


class UserModel(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), unique=True)
    email = Column(String(length=250))
    password = Column(String(length=50))
    is_active = Column(Boolean(), default=True)


    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    