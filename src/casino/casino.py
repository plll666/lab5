import random

from src.players.player import Player
from src.players.player_collection import PlayerCollection
from src.gooses.goose_collection import GooseCollection
from src.gooses.Goose import Goose, WarGoose, HonkGoose
from src.casino.casino_balance import CasinoBalance
from src.casino.chip import Chip


class Casino:
    def __init__(self):
        self.players = PlayerCollection()
        self.gooses = GooseCollection()
        self.balances = CasinoBalance()
        self.events = [
            self.event_player_bet,
            self.event_player_win,
            self.event_wargoose_attack,
            self.event_honkgoose_honk,
            self.event_goose_steal,
            self.event_combine_gooses,
            self.event_player_panics,
        ]

    def register_player(self, player: Player):
        if not isinstance(player, Player):
            raise TypeError("Это не игрок")
        self.players.add(player)
        self.balances[player.name] = player.balance
        print(f"[Casino] Зарегистрирован игрок {player.name} (баланс {player.balance})")

    def unregister_player(self, player_name: str):
        p = self.players.remove(player_name)
        del self.balances[p.name]
        print(f"[Casino] Игрок {p.name} удалён из казино")

    def register_goose(self, goose: Goose):
        if not isinstance(goose, (Goose, WarGoose, HonkGoose)):
            raise TypeError("Это не гусь")
        self.gooses.add(goose)
        print(f"[Casino] Гусь {goose.name} зарегистрирован")

    def unregister_goose(self, goose):
        removed = self.gooses.remove(goose)
        print(f"[Casino] Гусь {removed.name} удалён")
        return removed

    def get_random_player(self):
        if len(self.players) == 0:
            return None
        return random.choice(list(self.players))

    def get_random_goose(self):
        if len(self.gooses) == 0:
            return None
        return random.choice(self.gooses)

    def event_player_bet(self):
        player = self.get_random_player()
        if player is None:
            return print("[Event] Нет игроков для ставки")

        if player.balance > 0:
            return print(f"[Event] {player.name} не может ставить (нет средств)")

        bet_value = random.randint(1, max(1, player.balance // 2))
        bet = Chip(bet_value)

        old = player.balance
        player.balance = max(0, player.balance - bet_value)
        self.balances[player.name] = player.balance

        print(f"[Bet] {player.name} ставит {bet}, баланс: {old} -> {player.balance}")

    def event_player_win(self):
        player = self.get_random_player()
        if player is None:
            return print("[Event] Нет игроков для выигрыша")

        chip = Chip(random.randint(5, 20))
        old = player.balance

        player.balance += chip.value
        self.balances[player.name] = player.balance

        print(f"[Event] {player.name} выиграл {chip}, {old} -> {player.balance}")

    def event_wargoose_attack(self):
        war_gooses = [g for g in self.gooses if isinstance(g, WarGoose)]
        if not war_gooses:
            return print("[Event] Боевых гусей нет")

        war_g = random.choice(war_gooses)
        player = self.get_random_player()
        if player is None:
            return print("[Event] Нет игроков для атаки")

        damage = Chip(war_g.honk_volume + random.randint(1, 50))
        old = player.balance

        player.balance = max(0, player.balance - damage.value)
        self.balances[player.name] = player.balance

        print(f"[Event] WarGoose {war_g.name} атаковал {player.name}: -{damage}, {old} -> {player.balance}")

    def event_honkgoose_honk(self):
        honk_gooses = [g for g in self.gooses if isinstance(g, HonkGoose)]
        if not honk_gooses:
            return print("[Event] HonkGoose отсутствуют")

        honk = random.choice(honk_gooses)
        players = list(self.players)
        if not players:
            return print("[Event] Нет игроков")

        attacked = [p for p in players if random.random() < 0.5]
        if not attacked:
            attacked = [random.choice(players)]

        result = honk(attacked)
        for name, delta in result.items():
            player = self.players.find_by_name(name)
            if player is None:
                continue
            old = player.balance

            new_balance = max(0, player.balance + delta)

            player.balance = new_balance
            self.balances[player.name] = new_balance
            sign = "+" if delta >= 0 else ""
            print(f"[Event] Honk {honk.name} -> {player.name}: {sign}{delta}: {old} -> {new_balance}")

    def event_goose_steal(self):
        goose = self.get_random_goose()
        player = self.get_random_player()
        if goose is None or player is None:
            return print("[Event] Нужен и гусь, и игрок")

        steal_value = random.randint(1, max(1, min(player.balance, 10)))
        steal = Chip(steal_value)
        old = player.balance

        player.balance = max(0, player.balance - steal.value)
        self.balances[player.name] = player.balance

        print(f"[Event] {goose.name} украл {steal} у {player.name}: {old} -> {player.balance}")

    def event_combine_gooses(self):
        if len(self.gooses) < 2:
            return print("[Event] Мало гусей для объединения")

        gooses_list = list(self.gooses)
        g1, g2 = random.sample(gooses_list, 2)
        new_goose = g1 + g2

        self.gooses.add(new_goose)
        for g in self.gooses:
            if g is g1 or g is g2:
                self.gooses.remove(g)

        print(f"[Event] Объединены гуси: {g1.name} + {g2.name} -> {new_goose.name}")

    def event_player_panics(self):
        player = self.get_random_player()
        if player is None:
            return print("[Event] Нет игроков")

        old = player.balance

        if random.random() < 0.2:
            loss = Chip(old)
        else:
            loss = Chip(random.randint(1, max(1, old // 4)))

        player.balance = max(0, player.balance - loss.value)
        self.balances[player.name] = player.balance

        print(f"[Event] {player.name} потерял {loss}: {old} -> {player.balance}")

    def step(self):
        event = random.choice(self.events)
        print(f"\n[Step] Выполняется: {event.__name__}")
        event()

    def run_simulation(self, steps: int = 20, seed: int | None = None):
        if seed is not None:
            random.seed(seed)
            print(f"[Simulation] Установлен seed={seed}")

        print("\n[Simulation] НачалоО")
        for i in range(1, steps + 1):
            print(f"\n[Simulation] Шаг {i}/{steps}")
            self.step()

        print("\n[Simulation] Конец")
        print("\n[Simulation] Финальные балансы:")
        for p in self.players:
            print(f" - {p.name}: {p.balance}")
