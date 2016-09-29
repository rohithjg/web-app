from sqlalchemy.types import Integer, String, Date
from sqlalchemy.schema import Column
from model.engine import *


class Contact(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key= True)
    companyname = Column(String(80), unique= True)
    date = Column(Date,nullable=False)
    notes = Column(String(80))

users = Contact.__table__


