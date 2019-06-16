#execute this script before starting your python application

import sys
#for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import sessionmaker

#for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

#for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

#for configuration
from sqlalchemy import create_engine

from models import *

#create declarative_base instance
Base = declarative_base()

#we'll add classes here
#we create the class Book and extend it from the Base Class.
class Thing(Base):
   __tablename__ = 'thing'

   thingId = Column(Integer, primary_key=True)
   name = Column(String(250), nullable=False)
   category = Column(String(250), nullable=False)
   status = Column(String(250))
   user = Column(String(250))
   cost = Column(String(250))
   desc = Column(String(250))

#creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///rat.db')

Base.metadata.create_all(engine)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
session = DBSession()

thingOne = Thing(name="Lawn Mower", category="toolsAndEquipment", status="true", user="blank", cost=99, desc="Yo I am a rusty old Lawn Mower, Rent Me")
session.add(thingOne)
session.commit()
