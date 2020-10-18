from users.models import Profile


def test_profile_str(profile_foo: Profile) -> None:
    assert str(profile_foo) == str(profile_foo.user)
