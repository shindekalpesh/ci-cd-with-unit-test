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


def test_add_jobs(person: Person):
    person.add_job("Pilot")
    assert person.jobs == ["Software Developer", "Pilot"]


def test_no_surname(person: Person):
    '''
    Not using above fixture, instead using hardcoded one for this particular test func.
    '''
    person.name = "Thomas"
    assert not person.last_name