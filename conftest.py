import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def client():
    return APIClient()
