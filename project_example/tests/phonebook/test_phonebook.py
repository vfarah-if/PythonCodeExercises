from phonebook.phonebook import PhoneBook
import unittest


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    # Example of where you clean up resource
    def tearDown(self) -> None:
        return super().tearDown()

    def setupWith(self, name, phone_no):
        self.phonebook.add(name, phone_no)

    def test_add_creates_a_phone_book_entry(self):
        self.setupWith("Bob", "1234")

        self.assertEqual(len(self.phonebook.phone_numbers), 1)
        self.assertDictEqual(self.phonebook.phone_numbers, {"Bob": "1234"})

    def test_lookup_by_name(self):
        self.setupWith("Bob", "12345")

        number = self.phonebook.lookup("Bob")

        self.assertEqual("12345", number)

    def test_raises_key_error_when_name_not_found(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("UserThatDoesNotExist")

    # @unittest.skip("Showcase the skip mechanism")
    def test_is_consistent_when_there_are_no_duplicates(self):
        self.setupWith(name="Bob", phone_no="12345")

        self.setupWith("Sue", "23456")

        self.assertTrue(self.phonebook.is_consistent())

    def test_is_not_consistent_when_there_are_duplicate_values(self):
        self.setupWith(name="Bob", phone_no="12345")
        self.assertTrue(self.phonebook.is_consistent())

        self.setupWith("Jane", "12345")

        self.assertFalse(self.phonebook.is_consistent())
