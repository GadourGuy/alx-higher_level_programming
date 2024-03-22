#!/usr/bin/python3
"""making module_state to work with"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
	"""state class with id attribute"""

	__tablename__ = 'states'
	id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
	name = Column(String(128), nullable=False)
