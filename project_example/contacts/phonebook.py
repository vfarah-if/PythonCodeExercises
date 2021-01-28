class PhoneBook:
    
    def __init__(self):
        self.phone_numbers = {}

    def add(self, name: str, phone_no: any):
        self.phone_numbers[name.strip()] = phone_no

    def lookup(self, name: str):
        return self.phone_numbers[name]

    def is_consistent(self):
        unique_values = set(self.phone_numbers.values());
        return len(self.phone_numbers) == len(unique_values);
