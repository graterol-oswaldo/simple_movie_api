import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sql_file_name:str = "../database.sqlite"
base_dir:str = os.path.dirname(os.path.realpath(__file__))
database_url:str = f"sqlite:///{os.path.join(base_dir,sql_file_name)}"

engine = create_engine(database_url, echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
