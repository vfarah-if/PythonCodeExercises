import random


class SSOToken:
    def __init__(self):
        self.id = random.randrange(1_00_000)

    def __eq__(self, o: object) -> bool:
        return self.id == o.guid

    def __repr__(self) -> str:
        return str(self.id)
