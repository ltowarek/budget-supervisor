from users.models import Profile


def test_profile_is_created_when_user_is_created(user_foo):
    assert len(Profile.objects.all()) == 1
    assert hasattr(user_foo, "profile")


def test_profile_is_not_created_when_user_is_updated(user_foo):
    assert len(Profile.objects.all()) == 1
    user_foo.username = "abc"
    user_foo.save()
    assert len(Profile.objects.all()) == 1


def test_profile_str(user_foo):
    assert str(user_foo.profile) == str(user_foo)


def test_profile_create_in_saltedge(profile_foo, mock_saltedge):
    assert len(mock_saltedge.customers) == 0
    assert profile_foo.external_id is None
    Profile.objects.create_in_saltedge(profile_foo, mock_saltedge)
    assert len(mock_saltedge.customers) == 1
    assert profile_foo.external_id is not None


def test_profile_remove_from_saltedge(profile_foo_external, mock_saltedge):
    assert len(mock_saltedge.customers) == 1
    Profile.objects.remove_from_saltedge(profile_foo_external, mock_saltedge)
    assert len(mock_saltedge.customers) == 0
    assert profile_foo_external.external_id is None
