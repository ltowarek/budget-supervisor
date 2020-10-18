from users.models import Profile, User


def test_profile_is_created_when_user_is_created(user_foo: User) -> None:
    assert len(Profile.objects.all()) == 1
    assert hasattr(user_foo, "profile")


def test_profile_is_not_created_when_user_is_updated(user_foo: User) -> None:
    assert len(Profile.objects.all()) == 1
    user_foo.username = "abc"
    user_foo.save()
    assert len(Profile.objects.all()) == 1
