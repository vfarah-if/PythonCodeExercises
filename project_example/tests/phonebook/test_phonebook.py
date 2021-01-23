from phonebook.phonebook import PhoneBook
import unittest

class PhoneBookTest(unittest.TestCase):
    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add("Bob", "12345")
        
        number = phonebook.lookup("Bob")
        
        self.assertEqual("12345", number)

    def test_raises_key_error_when_name_not_found(self):
        phonebook = PhoneBook()

        with self.assertRaises(KeyError):
            phonebook.lookup("UserThatDoesNotExist")