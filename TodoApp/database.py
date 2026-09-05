from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
#
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SQLALCHEMY_DATABASE_URL = 'postgresql://fastapi_owsd_user:7nQULPwBZmq1EsmJMzsV9kSv4bq5k5uW@dpg-dae6jq740ujc73e1ct1g-a.singapore-postgres.render.com/fastapi_owsd'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
