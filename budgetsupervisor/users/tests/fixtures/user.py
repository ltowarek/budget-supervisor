import pytest


@pytest.fixture
def user_factory(db, django_user_model):
    def create_user(
        username,
        password="password",
        first_name="foo",
        last_name="bar",
        email="foo@bar.com",
        is_staff=False,
        is_superuser=False,
        is_active=True,
    ):
        return django_user_model.objects.create(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )

    return create_user


@pytest.fixture
def user_foo(user_factory):
    return user_factory(username="foo")
