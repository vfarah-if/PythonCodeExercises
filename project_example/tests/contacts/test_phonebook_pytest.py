import pytest
from contacts.phonebook import PhoneBook


def test_add_creates_a_phone_book_entry():
    phonebook = PhoneBook()
    phonebook.add("Bob", "1234")

    assert len(phonebook.phoneNumbers) == 1
    assert phonebook.phoneNumbers == {"Bob": "1234"}


def test_add_number_phone_book_entry():
    phonebook = PhoneBook()

    phonebook.add("Bob", 1234)

    assert len(phonebook.phoneNumbers) == 1
    assert phonebook.phoneNumbers == {"Bob": 1234}


def test_lookup_by_name():
    phonebook = PhoneBook()
    phonebook.add("Bob", 1234)

    actual = phonebook.lookup("Bob")

    assert actual == 1234


def test_raises_key_error_when_name_not_found():
    phonebook = PhoneBook()

    with pytest.raises(KeyError):
        phonebook.lookup("UserThatDoesNotExist")
