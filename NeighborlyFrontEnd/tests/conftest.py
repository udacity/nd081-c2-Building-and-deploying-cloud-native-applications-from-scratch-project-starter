import pytest

@pytest.fixture
def client():
    import neighborly
    neighborly.app.config['TESTING'] = True
    return neighborly.app.test_client()

