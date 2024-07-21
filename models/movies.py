from config.database import Base
from sqlalchemy import Column, Integer, String, Float


class MovieModel(Base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=150), unique=True)
    overview = Column(String(length=300))
    year = Column(Integer)
    rating = Column(Float(precision=2))
    category = Column(String(length=50))
