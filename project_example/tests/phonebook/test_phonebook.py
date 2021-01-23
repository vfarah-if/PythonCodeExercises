from phonebook.phonebook import PhoneBook
import unittest


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    # Example of where you clean up resource
    def tearDown(self) -> None:
        return super().tearDown()

    def test_lookup_by_name(self):
        self.phonebook.add("Bob", "12345")

        number = self.phonebook.lookup("Bob")

        self.assertEqual("12345", number)

    def test_raises_key_error_when_name_not_found(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("UserThatDoesNotExist")

    # @unittest.skip("Showcase the skip mechanism")
    def test_is_consistent_when_there_are_no_duplicates(self):
        self.phonebook.add(name="Bob", phone_no="12345")
        self.assertTrue(self.phonebook.is_consistent())

        self.phonebook.add("Sue", "23456")
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_not_consistent_when_there_are_duplicate_values(self):
        self.phonebook.add(name="Bob", phone_no= "12345")
        self.assertTrue(self.phonebook.is_consistent())

        self.phonebook.add("Jane", "12345")
        self.assertFalse(self.phonebook.is_consistent())
