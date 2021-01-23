from phonebook.phonebook import PhoneBook
import unittest

class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    # Example of where you 
    def tearDown(self) -> None:
        return super().tearDown()

    def test_lookup_by_name(self):        
        self.phonebook.add("Bob", "12345")
        
        number = self.phonebook.lookup("Bob")
        
        self.assertEqual("12345", number)

    def test_raises_key_error_when_name_not_found(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("UserThatDoesNotExist")

    @unittest.skip("Showcase the skip mechanism")
    def test_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())