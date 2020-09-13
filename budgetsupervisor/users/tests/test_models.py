from users.models import Profile
import swagger_client as saltedge_client


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


def test_profile_create_in_saltedge(
    profile_foo, customers_api, saltedge_customer_factory
):
    data = saltedge_customer_factory(id="123")
    customers_api.customers_post.return_value = saltedge_client.CreatedCustomerResponse(
        data=data
    )

    assert profile_foo.external_id is None
    Profile.objects.create_in_saltedge(profile_foo, customers_api)
    assert profile_foo.external_id == 123


def test_profile_remove_from_saltedge(profile_foo_external, customers_api):
    data = saltedge_client.RemovedCustomerResponseData(
        deleted=True, id=str(profile_foo_external.external_id)
    )
    customers_api.customers_customer_id_delete.return_value = saltedge_client.RemovedCustomerResponse(
        data=data
    )

    assert profile_foo_external.external_id is not None
    Profile.objects.remove_from_saltedge(profile_foo_external, customers_api)
    assert profile_foo_external.external_id is None
