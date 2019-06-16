import sys
#for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

#for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

#for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

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
   