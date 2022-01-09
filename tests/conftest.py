import pytest

@pytest.fixture
def api_url():
    return "http://0.0.0.0:8000/api"

@pytest.fixture
def item_url():
    return "http://0.0.0.0:8000/items"