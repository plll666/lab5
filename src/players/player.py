class Player:
    def __init__(self, name: str, balance: int):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if not isinstance(balance, int):
            raise TypeError("Баланс должен быть целым числом")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")

        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"Игрок: {self.name}, баланс: {self.balance}"