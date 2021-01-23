from datetime import date, timedelta
from typing import Generator

class Prescription:
    def __init__(self, description: str, dispenseDate: date, daysSupply: int):
        self.description = description
        self.dispenseDate = dispenseDate
        self.daysSupply = daysSupply

    def daysTaken(self) -> Generator:
        all_days = (self.dispenseDate + timedelta(days=i)
                    for i in range(self.daysSupply))
        return (day for day in all_days if day < date.today())
    
    def toString(self):
        return f"{self.description} should be dispensed on the '{self.dispenseDate}' with only {self.daysSupply} days supply"
