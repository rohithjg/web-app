from sqlalchemy import create_engine
engine = create_engine('mysql://root:maga123@localhost/pilot', echo=False)
from sqlalchemy.types import Integer, String
from sqlalchemy.schema import Column
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Contact(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key= True)
    firstname = Column(String(80), nullable= False)
    lastname = Column(String(80), nullable= False)
    comapanyname = Column(String(80), unique= True)
    notes = Column(String(80))

users = Contact.__table__
metadata = Base.metadata
metadata.create_all(engine)

