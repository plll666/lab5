from src.gooses.Goose import WarGoose
from src.players.player import Player

war_goose = WarGoose("БоевойГусь", 30)
player = Player("ТестовыйИгрок", 100)

print(f"До атаки: баланс игрока = {player.balance}")
print(f"Сила гуся: honk_volume = {war_goose.honk_volume}")

for i in range(3):
    old_balance = player.balance
    damage = war_goose.attack(player)
    new_balance = player.balance

    print(f"\nАтака {i + 1}:")
    print(f"Нанесенный ущерб: {damage}")
    print(f"Баланс: {old_balance} -> {new_balance}")
    print(f"Изменение: {new_balance - old_balance}")

    player.balance = 100

print("\nТест с разными балансами")
test_balances = [10, 50, 100, 150]
for balance in test_balances:
    player.balance = balance
    old = player.balance
    war_goose.attack(player)
    print(f"Начальный баланс: {old}, Конечный баланс: {player.balance}, Разница: {player.balance - old}")