#!/usr/bin/python3
"""
Python file that contains the class definition of a State and an instance
Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    Create Class City
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
