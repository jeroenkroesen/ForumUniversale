import os
from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

# Setup the database
engine = create_engine(current_app.config['DATABASE'], future=True)
DbSession = scoped_session(sessionmaker(bind=engine))
ModelBase = declarative_base()


# Example init_db function
def init_db():
    from . import models
    ModelBase.metadata.create_all(bind=engine)
