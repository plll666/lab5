from src.players.player import Player

class PlayerCollection:
    def __init__(self):
        self._players = []

    def add(self, player: Player) -> None:
        if not isinstance(player, Player):
            raise TypeError("Можно добавлять только Player")

        if player in self._players:
            raise ValueError("Игрок уже в коллекции")

        self._players.append(player)
        print(f"Добавлен игрок {player.name} с балансом: {player.balance}")

    def remove(self, player):
        if isinstance(player, Player):
            if player not in self._players:
                raise ValueError("Игрок не найден")
            self._players.remove(player)
            print(f"Удалён игрок: {player.name}")
            return player

        elif isinstance(player, str):
            for p in self._players:
                if p.name == player:
                    self._players.remove(p)
                    print(f"Удалён игрок: {p.name}")
                    return p
            raise ValueError("Игрок с таким именем не найден")
        else:
            raise TypeError("remove принимает Player или имя")

    def __len__(self):
        return len(self._players)

    def __iter__(self):
        return iter(self._players)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return PlayerCollection(self._players[index])
        return self._players[index]

    def __contains__(self, item):
        if isinstance(item, Player):
            return any(p is item for p in self._players)
        if isinstance(item, str):
            return any(p.name == item for p in self._players)
        return False

    def find_by_name(self, name):
        for p in self._players:
            if p.name == name:
                return p
        return None

    def find_by_balance_range(self, min_balance=0, max_balance=float('inf')):
        result = PlayerCollection()
        for p in self._players:
            if min_balance <= p.balance <= max_balance:
                result.add(p)
        return result