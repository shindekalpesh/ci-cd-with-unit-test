from src.person import Person

import pytest

@pytest.fixture()
def person():
    return Person("Thomas Shelby", 34, jobs=["Software Developer"])
    

def test_init():
    person = 
    assert person.name == "Thomas Shelby"
    assert person.age == 34
    assert person.jobs == ["Software Developer"]


def test_first_name():
    person = Person("Thomas Shelby", 34, jobs=["Software Developer"])
    assert person.first_name == "Thomas"