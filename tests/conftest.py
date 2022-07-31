from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
import pytest
import os
import sys
import tempfile

try:
    sys.path.append(os.getcwd()+"/src")
except Exception:
    pass

from main import app
from database import get_db
import models

engine = create_engine("sqlite:///test.db")
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind = engine)

@pytest.fixture(scope="session")
def session():
    session = TestingSessionLocal()

    with open("data/insert_book.sql", "r") as f:
        session.execute(f.read())
        session.commit()
        # session.close()
    yield session
    os.remove("test.db")

@pytest.fixture(scope="function")
def client(session) -> TestClient:
    def get_db_test():
        db = session
        try:
            yield db
        finally:
            db.close()

    with TestClient(app) as client:
        app.dependency_overrides[get_db] = get_db_test
        yield client

