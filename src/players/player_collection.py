from src.players.player import Player

class PlayerCollection:
    def __init__(self):
        self._players = []

    def add(self, player : Player) -> None:
        if not isinstance(player, Player):
            raise TypeError("Можно добавлять только Player")

        if player in self._players:
            raise ValueError("Игрок уже в коллекции")

        self._players.append(player)

        print(f"Добавлен игрок {player.name} с балансом: {player.balance}")

    def __len__(self) -> int:
        return len(self._players)

    def __getitem__(self, index):
        return self._players[index]

    def __iter__(self):
        return iter(self._players)

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
