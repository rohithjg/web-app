from sqlalchemy.types import Integer, String, Date
from sqlalchemy.schema import Column
from model.engine import *
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Contact(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key= True)
    companyname = Column(String(80), unique= True)
    date = Column(Date,nullable=False)
    notes = Column(String(80))

users = Contact.__table__
metadata = Base.metadata
metadata.create_all(engine)

