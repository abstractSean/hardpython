import pytest

from .dictionary import Dictionary

@pytest.fixture
def states():
    states = Dictionary()
    states.set('Oregon', 'OR')
    states.set('Florida', 'FL')
    states.set('California', 'CA')
    states.set('New York', 'NY')
    states.set('Michigan', 'MI')
    return states

@pytest.fixture
def cities():
    cities = Dictionary()
    cities.set('CA', 'San Francisco')
    cities.set('MI', 'Detroit')
    cities.set('FL', 'Jacksonville')
    cities.set('NY', 'New York')
    cities.set('OR', 'Portland')
    return cities

def test_get(states, cities):
    assert cities.get('NY') == 'New York'
    assert cities.get('OR') == 'Portland'

    assert states.get('Michigan') == 'MI'
    assert states.get('Florida') == 'FL'

    assert cities.get(states.get('Michigan')) == 'Detroit'
    assert cities.get(states.get('Florida')) == 'Jacksonville'

def test_list(states, cities):
    states.list()
    cities.list()

def test_get_none(states):
    state = states.get('Texas')
    assert state == None

def test_get_default(cities):
    city = cities.get('TX', 'Does Not Exist')
    assert city == 'Does Not Exist'
