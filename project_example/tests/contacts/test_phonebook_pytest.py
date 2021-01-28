from pytest import raises, fixture
import pytest
from contacts.phonebook import PhoneBook


# Moved to conftest in the folder to share but can be used here
# @fixture
# def phonebook():
#     # Fixture document comment
#     "Provides an empty phonebook"
#     return PhoneBook()

@pytest.mark.slow
def test_add_creates_a_phone_book_entry(phonebook):
    phonebook.add("Bob", "1234")

    assert len(phonebook.phone_numbers) == 1
    assert phonebook.phone_numbers == {"Bob": "1234"}


def test_add_number_phone_book_entry(phonebook):
    phonebook.add("Bob", 1234)

    assert len(phonebook.phone_numbers) == 1
    assert phonebook.phone_numbers == {"Bob": 1234}


def test_lookup_by_name(phonebook):
    phonebook.add("Bob", 1234)

    actual = phonebook.lookup("Bob")

    assert actual == 1234


def test_raises_key_error_when_name_not_found(phonebook):
    with raises(KeyError):
        phonebook.lookup("UserThatDoesNotExist")


def test_is_consistent_when_there_are_no_duplicates(phonebook):
    phonebook.add("Bob", 12345)
    assert phonebook.is_consistent() is True

    phonebook.add("Sue", 23456)
    assert phonebook.is_consistent() is True


def test_is_not_consistent_when_there_are_duplicate_numbers(phonebook):
    phonebook.add("Bob", 12345)
    assert phonebook.is_consistent() is True

    phonebook.add("Sue", 12345)
    assert phonebook.is_consistent() is False
