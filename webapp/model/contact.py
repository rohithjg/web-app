# Create engine is essential for connecting to the database
from sqlalchemy import create_engine
engine = create_engine('mysql://root:maga123@localhost/pilot', echo=False)

# ORM's handle to db is Session, we need it to talk to the database
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

from sqlalchemy.types import Integer, String, Date
from sqlalchemy.schema import Column
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Contact(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key= True)
    firstname = Column(String(80), nullable= False)
    lastname = Column(String(80), nullable= False)
    companyname = Column(String(80), unique= True)
    date = Column(Date,nullable=False)
    notes = Column(String(80))

users = Contact.__table__
metadata = Base.metadata
metadata.create_all(engine)

