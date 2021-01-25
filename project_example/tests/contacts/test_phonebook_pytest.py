from pytest import raises, fixture
from contacts.phonebook import PhoneBook


# Moved to conftest in the folder to share but can be used here
# @fixture
# def phonebook():
#     # Fixture document comment
#     "Provides an empty phonebook"
#     return PhoneBook()


def test_add_creates_a_phone_book_entry(phonebook):
    phonebook.add("Bob", "1234")

    assert len(phonebook.phoneNumbers) == 1
    assert phonebook.phoneNumbers == {"Bob": "1234"}


def test_add_number_phone_book_entry(phonebook):
    phonebook.add("Bob", 1234)

    assert len(phonebook.phoneNumbers) == 1
    assert phonebook.phoneNumbers == {"Bob": 1234}


def test_lookup_by_name(phonebook):
    phonebook.add("Bob", 1234)

    actual = phonebook.lookup("Bob")

    assert actual == 1234


def test_raises_key_error_when_name_not_found(phonebook):
    with raises(KeyError):
        phonebook.lookup("UserThatDoesNotExist")
