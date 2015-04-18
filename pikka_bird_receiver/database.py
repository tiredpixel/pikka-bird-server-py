import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


db_engine  = create_engine(os.environ['DATABASE_URI'])
db_session = scoped_session(sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=db_engine))

Base = declarative_base()
Base.query = db_session.query_property()

Base.metadata.reflect(db_engine)
