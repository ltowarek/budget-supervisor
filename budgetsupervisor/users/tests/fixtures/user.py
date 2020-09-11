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


@pytest.fixture
def profile_factory(db, user_foo):
    def create_profile(
        user=user_foo, external_id=None,
    ):
        profile = user.profile
        profile.external_id = external_id
        profile.save()
        return profile

    return create_profile


@pytest.fixture
def profile_foo(profile_factory):
    return profile_factory()


@pytest.fixture
def profile_foo_external(profile_factory, mock_saltedge):
    data = mock_saltedge.create_customer("foo")
    return profile_factory(external_id=data["data"]["id"])
