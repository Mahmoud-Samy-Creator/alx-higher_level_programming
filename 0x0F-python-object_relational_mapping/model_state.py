#!/usr/bin/python3

"""
    this module contains a Base and State class
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
Base = declarative_base()


class State(Base):
    """States class
    Args:
        Base (declarative): declarative base to inherit from
        Attributes:
            id (int)
            name (string)
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
