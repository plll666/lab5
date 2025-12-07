
class CasinoBalance:
    def __init__(self):
        self._balances = {}

    def __getitem__(self, key) -> int:
        if key in self._balances:
            return self._balances[key]
        raise KeyError(f"Игрок {key} не найден")

    def __setitem__(self, key, new_value):
        if not isinstance(new_value, int):
            raise TypeError("Баланс должен быть целым числом")

        if new_value < 0:
            raise ValueError("Баланс не может быть отрицательным")

        if key in self._balances:
            old_value = self._balances[key]
            self._balances[key] = new_value
            print(f"Баланс игрока {key} изменён: {old_value} → {new_value}")
        else:
            self._balances[key] = new_value
            print(f"Добавлен новый игрок {key} с балансом {new_value}")

    def __len__(self) -> int:
        return len(self._balances)

    def __iter__(self):
        return iter(self._balances)

    def add_player(self, name: str, balance: int):

        if not isinstance(balance, int):
            raise TypeError("Баланс должен быть целым числом")

        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")

        if name not in self._balances:
            self._balances[name] = balance
            print(f"Добавлен счет игрока {name} с балансом {balance}")
        else:
            raise ValueError(f"Счет игрока {name} уже существует")

    def remove_player(self, name: str):
        if name in self._balances:
            old = self._balances[name]
            del self._balances[name]
            print(f"Удалён счёт игрока {name} с балансом {old}")
        else:
            raise ValueError(f"Счета игрока {name} не существует")

    def total_balance(self) -> int:
        total = 0
        for balance in self._balances.values():
            total += balance
        return total



