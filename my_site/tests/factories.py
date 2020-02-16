import factory
from django.contrib.auth.models import User
from ..models import TodoTask


class UserFactory(factory.DjangoModelFactory):
    email = factory.Sequence('user-{}@example.com'.format)
    name = factory.Sequence('User {}'.format)
    password = factory.PostGenerationMethodCall('set_password', None)

    class Meta:
        model = User


class TodoTaskFactory(factory.DjangoModelFactory):

    class Meta:
        model = TodoTask
