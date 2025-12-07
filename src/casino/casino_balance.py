class CasinoBalance:
    def __init__(self):
        self._balances = {}

    def __getitem__(self, key) -> int:
        if not isinstance(key, str):
            raise TypeError("Ключ должен быть строкой")
        if key in self._balances:
            return self._balances[key]
        raise KeyError(f"Игрок {key} не найден")

    def __setitem__(self, key, new_value):
        if not isinstance(key, str):
            raise TypeError("Имя игрока должно быть строкой")
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

    def __delitem__(self, key):
        if key in self._balances:
            old = self._balances[key]
            del self._balances[key]
            print(f"Удалён счёт игрока {key} с балансом {old}")
        else:
            raise KeyError(f"Счета игрока {key} не существует")

    def __len__(self) -> int:
        return len(self._balances)

    def __iter__(self):
        return iter(self._balances)

    def __contains__(self, key):
        return key in self._balances

    def add_player(self, name: str, balance: int):
        self[name] = balance

    def remove_player(self, name: str):
        del self[name]

    def total_balance(self) -> int:
        return sum(self._balances.values())

    def find_players_by_balance(self, min_balance=0, max_balance=float('inf')):
        result = {}
        for name, balance in self._balances.items():
            if min_balance <= balance <= max_balance:
                result[name] = balance
        return result