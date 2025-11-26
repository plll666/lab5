from random import randint
from src.players.player import Player

class Goose:
    def __init__(self, name: str, honk_volume: int):
        self.name = name
        self.honk_volume = honk_volume


class WarGoose(Goose):
    def attack(self,  player: Player):
        damage = self.honk_volume + randint(1, 10)
        player.balance -= damage
        return f"Игрок потерял {damage} денег, баланс: {player.balance}"


class HonkGoose(Goose):
    def __call__(self, players: list):
        result = {}
        for player in players:
            damage = randint(-self.honk_volume, self.honk_volume)
            player.balance = max(0, player.balance + damage)
            result[player.name] = player.balance
            if damage > 0:
                print(f"Игрок: {player.name}, получил {damage}")
            if damage < 0:
                print(f"Игрок: {player.name}, потерял{damage}")
            if damage == 0:
                print(f"у игрока: {player.name} ничего не поменялось")
        return result
