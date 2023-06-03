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
        return {
            "<User(name, lastname, username)>"
            "name": self.name
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

class character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), primary_key=False)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    hair_color = Column(String(250), primary_key=False)
    eye_color = Column(String(250), primary_key=False)
    skin_color = Column(String(250), primary_key=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), primary_key=False)
    hoeworld = Column(Strin(250), primary_key=False)
    
class fav_character(Base):
    __tablename__ = "fav_character"
    id = Column(Integer, ForeignKey("user.id"))
    user_id = Column(Integer, ForeignKey("user.name"))
    character_id = Column(Integer, ForeignKey("character.id"))
    
class planets(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(250), primary_key=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, primary_key=False)
    climate = Column(String(250), primary_key=False)
    gravity = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)


class fav_planets(Base):
    __tablename__ = "fav_planets"
    id = Column(Integer, ForeignKey("user.id"))
    user_id = Column(Integer, ForeignKey("user.name"))
    planets_id = Column(Integer, ForeignKey("planet.id"))
    
