from src.person import Person

def test_init():
    person = Person("Thomas Shelby", 34, jobs=["Software Developer"])
    assert person.name == "Thomas Shelby"
    assert person.age == 34
    assert person.jobs == ["Software Developer"]


def test_first_name():
    person = Person("Thomas Shelby", 34, jobs=["Software Developer"])
    assert person.first_name == "Thomas"