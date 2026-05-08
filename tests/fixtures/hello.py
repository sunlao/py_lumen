from pytest import fixture
from hello.world import World


@fixture
def world():
    return World()
