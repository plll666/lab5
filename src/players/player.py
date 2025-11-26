
class Player:
    def __init__(self,name: str, balance: int):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"Игрок: {self.name}, баланс: {self.balance}"