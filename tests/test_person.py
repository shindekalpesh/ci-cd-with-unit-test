from src.person import Person

import pytest

@pytest.fixture()
def person():
    return Person("Thomas Shelby", 34, jobs=["Software Developer"])
    

def test_init(person: Person):
    assert person.name == "Thomas Shelby"
    assert person.age == 34
    assert person.jobs == ["Software Developer"]


def test_first_name(person: Person):
    assert person.first_name == "Thomas"


def test_last_name(person: Person):
    assert person.last_name == "Shelby"


def test_celebrate_birthday(person: Person):
    person.celebrate_birthday()
    assert person.age == 35