import pytest
from fastapi.testclient import TestClient

from demo_setup.interface.api.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
