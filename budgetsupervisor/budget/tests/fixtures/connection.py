import pytest
from budget.models import Connection


@pytest.fixture
def connection_factory(db, user_foo):
    def create_connection(
        provider, user=user_foo, external_id=None,
    ):
        return Connection.objects.create(
            provider=provider, user=user, external_id=external_id
        )

    return create_connection


@pytest.fixture
def connection_foo(connection_factory):
    return connection_factory("foo")


@pytest.fixture
def connection_foo_external(connection_factory, profile_foo_external):
    return connection_factory(
        provider="foo", user=profile_foo_external.user, external_id=123
    )
