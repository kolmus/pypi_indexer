import pytest
from pypi_app.tests.utils import create_fake_items

@pytest.fixture
def create_items():
    create_fake_items()
    