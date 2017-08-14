#!/usr/bin/python3
"""
city model
"""
from model_state import State, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
