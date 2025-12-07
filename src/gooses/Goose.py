from random import randint
from src.players.player import Player

class Goose:
    def __init__(self, name, honk_volume):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if not isinstance(honk_volume, int):
            raise TypeError("Громкость должна быть числом")
        if honk_volume < 0:
            raise ValueError("Громкость не может быть отрицательной")
        self.name = name
        self.honk_volume = honk_volume

    def __add__(self, other):
        if not isinstance(other, Goose):
            return NotImplemented
        new_name = f"{self.name}&{other.name}"
        new_volume = self.honk_volume + other.honk_volume
        if type(self) is type(other):
            return type(self)(new_name, new_volume)
        return Goose(new_name, new_volume)


class WarGoose(Goose):
    def attack(self, player):
        if not isinstance(player, Player):
            raise TypeError("Можно атаковать только игрока")
        if not isinstance(player.balance, int):
            raise TypeError("Баланс игрока должен быть числом")
        damage = self.honk_volume + randint(1, 50)
        player.balance = max(0, player.balance - damage)
        return damage


class HonkGoose(Goose):
    def __call__(self, players):
        if not isinstance(players, (list, tuple)):
            raise TypeError("Должен быть передан список игроков")
        result = {}
        for p in players:
            if not isinstance(p, Player):
                raise TypeError("Элементы должны быть Player")
            delta = randint(-self.honk_volume, self.honk_volume)
            result[p.name] = delta
        return result
