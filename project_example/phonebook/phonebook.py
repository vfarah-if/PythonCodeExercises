class PhoneBook:
    
    def __init__(self):
        self.phoneNumbers = {}

    def add(self, name: str, phone_no: any):
        self.phoneNumbers[name.strip()] = phone_no

    def lookup(self, name: str):
        return self.phoneNumbers[name]

    def isConsistent(self):
        uniqueValues = set(self.phoneNumbers.values());
        return len(self.phoneNumbers) == len(uniqueValues);
