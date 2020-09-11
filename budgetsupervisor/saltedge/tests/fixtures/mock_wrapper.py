import pytest
from saltedge.tests.mocks import MockSaltEdgeWrapper


@pytest.fixture
def mock_saltedge_factory():
    def create_wrapper(app_id, secret, private_path):
        return MockSaltEdgeWrapper(app_id, secret, private_path)

    return create_wrapper


@pytest.fixture
def mock_saltedge(mock_saltedge_factory):
    app_id = "123"
    secret = "xyz"
    private_path = "foo.pem"
    return mock_saltedge_factory(app_id, secret, private_path)
