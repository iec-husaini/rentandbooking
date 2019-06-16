from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#Let us import our Book and Base classes from our database_setup.py file
from database_setup import Thing, Base

engine = create_engine('sqlite:///rat.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
session = DBSession()

thingOne = Thing(name="Lawn Mower", category="toolsAndEquipment", status="true", user="blank", cost=99, desc="I am a rusty old Lawn Mower, Rent Me")
session.add(thingOne)
session.commit()
