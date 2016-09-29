# Create engine is essential for connecting to the database
from sqlalchemy import create_engine
engine = create_engine('mysql://root:maga123@localhost/pilot', echo=False)

# ORM's handle to db is Session, we need it to talk to the database
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
from sqlalchemy.ext.declarative import declarative_base
# Maintains a catalogue of classes and tables relative to the database
Base = declarative_base()
# To create all the tables
Base.metadata.create_all(engine)
session=Session()