import pytest
from budget.models import Category


@pytest.fixture
def category_factory(db, user_foo):
    def create_category(name, user=user_foo):
        return Category.objects.create(name=name, user=user)

    return create_category


@pytest.fixture
def category_foo(category_factory):
    return category_factory("foo")
