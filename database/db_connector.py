from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base

def create_session():
    engine = create_engine('postgresql://testing:testing@postgres:5432/todo_db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    return Session()