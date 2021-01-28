from pytest import fixture
from contacts.phonebook import PhoneBook


@fixture
def phonebook():
    # Fixture document comment
    """Provides an empty phonebook"""
    return PhoneBook()
