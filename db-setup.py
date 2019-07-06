
#### CONFIGURATION ================================================
#### beginning of file config

import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

### create instance of declarative base ---------------------------
### lets sqlalchemy know that classes are dedicated to tables in db
Base = declarative_base() 

#### CLASSES FOR SQL TABLES =======================================

### create two tables with the tables corresponding to the DB

## table 1: for restaurants
class Restaurant(Base):

    ## set name of table for restaurants
    __tablename__ = 'restaurant'

    ## column 1: name can't be null, no row is created if so
    rest_name = Column(String(80), nullable = False)

    ## column 2: make this primary key of table
    rest_id = Column(Integer, primary_key = True)

## table 2: for menu-items:
class MenuItem(Base):

    ## set name of table for menu items
    __tablename__ = 'menu_item'

    ## col 1: name of menu item, cant be null
    item_name = Column(String(80), nullable = False)

    ## col 2: menu item ID, make primary key
    item_id = Column(Integer, primary_key = True)

    ## col 3: menu item van het maaltijd course
    item_course = Column(String(250))

    ## col 4: description of menu item
    item_price = Column(String(8))

    ## col 5: restaurant ID for menu item, make foregin-key to establish relationship with restaurant menu
    ## restaurant.rest_id: points to 'rest_id' col in table 'restaturant'
    restaurant_id = Column(Integer, ForeignKey('restaurant.rest_id'))

    ## col 6: relationship with class 'restaurant'
    restaurant = relationship(Restaurant)

#### CONFIGURATION ==================================================
#### end of file config

### write db to file in script dir:

## init DB with name, pass to SQL Alchemy engine
engine = create_engine('sqlite:///restaurantmenu.db')

## use SQL Alchemy engine to write file:
Base.metadata.create_all(engine)

