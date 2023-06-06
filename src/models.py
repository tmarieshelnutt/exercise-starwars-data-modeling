import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
# render_er(Base, 'diagram.png')

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    email = Column(String(250))
    user_name = Column(String(250))
    password = Column(String(250))

    def to_dict(self):
        return {}

class character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    skin_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    hoeworld = Column(Strin(250))

    def to_dict(self):
        return {}
    
class favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    item_type = Column(String(250))
    
    def to_dict(self):
        return {}

class planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), primary_key=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, primary_key=False)
    climate = Column(String(250), primary_key=False)
    gravity = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer)
    population = Column(Integer)

    def to_dict(self):
        return {}

class fav_planets(Base):
    __tablename__ = "fav_planets"
    id = Column(Integer, ForeignKey("user.id"))
    user_id = Column(Integer, ForeignKey("user.name"))
    planets_id = Column(Integer, ForeignKey("planet.id"))
    
    def to_dict(self):
        return {}
render_er(Base, 'diagram.png')
