import os
import tempfile
import pytest
from fastapi.testclient import TestClient

from main import init_db

init_db()

@pytest.fixture(scope="function")
def test_db():
    db_fd, db_path = tempfile.mkstemp()

    os.environ["DB_PATH"] = db_path

    init_db()

    yield db_path

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(test_db):
    from main import app
    return TestClient(app)