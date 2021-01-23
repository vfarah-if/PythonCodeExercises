class PhoneBook:
    
    def __init__(self):
        self.phone_numbers = {}

    def add(self, name: str, phone_no: str):
        self.phone_numbers[name.strip()] = phone_no.strip()

    def lookup(self, name: str):
        return self.phone_numbers[name]

