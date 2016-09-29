from sqlalchemy.types import Integer, String, Date
from sqlalchemy.schema import Column
from model.engine import *


class Register(Base):
    __tablename__= 'stakeholders'

    firstname = Column(String(80), nullable= False)
    lastname = Column(String(80), nullable= False)
    email = Column(String(80), primary_key= True)
    sex = Column(String(80), nullable= False)
    username = Column(String(80), unique= True)
    password = Column(String(80), unique= True)

stakeholders = Register.__table__


