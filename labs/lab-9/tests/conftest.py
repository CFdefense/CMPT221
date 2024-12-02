import os
import pytest

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert, select, text
from models import User

# contains table objects
Base = declarative_base()

# import environment variables from .env
load_dotenv()

db_name: str = os.getenv('db_name')
db_owner: str = os.getenv('db_owner')
db_pass: str = os.getenv('db_pass')
db_uri: str = f"postgresql://{db_owner}:{db_pass}@localhost/{db_name}"

# create db connection w/o Flask
# NOTE: creates new session for each test function
@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(db_uri) 
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # create tables
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    yield session
    session.close()
    # drop tables
    Base.metadata.drop_all(bind=engine)

# example fixture - user sign in input
# hint... can you do something similar for login?
@pytest.fixture
def sample_signup_input():
    return {'FirstName': 'Calista', 
            'LastName': 'Phippen', 
            'Email': 'calista.phippen1@marist.edu', 
            'PhoneNumber': '1234567891', 
            'Password': 'mypassword'
            }

# bad input for creating a user
@pytest.fixture
def sample_bad_signup():
    return {'FirstName':'123Christian',
            'LastName':'Farrell',
            'Email':'CFdefence@gmail.com',
            'PhoneNumber':'1234567891',
            'Password':'password',
           }