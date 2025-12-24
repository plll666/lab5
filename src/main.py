import typer
import shlex
import random

from src.casino.casino import Casino
from src.players.player import Player
from src.gooses.Goose import Goose, WarGoose, HonkGoose

app = typer.Typer()
casino = Casino()


@app.command()
def interactive():
    """
    Интерактивный режим казино
    """
    typer.echo("Казино и Гуси")
    typer.echo("Введите 'help' для списка команд")

    while True:
        try:
            raw = input().strip()
            if not raw:
                continue

            args = shlex.split(raw)
            cmd = args[0]

            if cmd in ("exit", "quit", "q"):
                typer.echo("Выход")
                break


            elif cmd == "help":
                print_commands()

            elif cmd == "add":
                handle_add(args[1:])

            elif cmd == "step":
                casino.step()

            elif cmd == "run":
                handle_run(args[1:])

            elif cmd == "status":
                print_status()

            elif cmd == "spawn":
                handle_spawn(args[1:])

            else:
                typer.echo("Неизвестная команда. Введите 'help'")

        except Exception as e:
            typer.echo(f"Ошибка: {e}")


def print_commands():
    typer.echo("""
Доступные команды:

  add player <name> <balance>
  add goose normal|war|honk <name> <honk_volume>

  spawn players <count>
  spawn geese <count>

  step
  run <steps> [seed=число]

  status
  help
  exit
""")



def handle_add(args):
    if not args:
        raise ValueError("add player / goose")

    kind = args[0]

    if kind == "player":
        name = args[1]
        balance = int(args[2])
        casino.register_player(Player(name, balance))

    elif kind == "goose":
        gtype = args[1]
        name = args[2]
        volume = int(args[3])

        if gtype == "normal":
            goose = Goose(name, volume)
        elif gtype == "war":
            goose = WarGoose(name, volume)
        elif gtype == "honk":
            goose = HonkGoose(name, volume)
        else:
            raise ValueError("Тип гуся: normal | war | honk")

        casino.register_goose(goose)

    else:
        raise ValueError("add player / add goose")


def handle_run(args):
    steps = int(args[0])
    seed = None

    for a in args[1:]:
        if a.startswith("seed="):
            seed = int(a.split("=")[1])

    casino.run_simulation(steps=steps, seed=seed)


def print_status():
    typer.echo("\nИгроки:")
    if len(casino.players) == 0:
        typer.echo("  (нет)")
    for p in casino.players:
        typer.echo(f"  - {p.name}: {p.balance}")
    typer.echo("\nГуси:")
    if len(casino.gooses) == 0:
        typer.echo("  (нет)")
    for g in casino.gooses:
        typer.echo(f"  - {g.name} ({type(g).__name__}, honk={g.honk_volume})")

    typer.echo("\nОбщий баланс:")
    typer.echo(f"  {casino.balances.total_balance()}\n")

def handle_spawn(args):
    if len(args) != 2:
        raise ValueError("Использование: spawn players/geese <count>")

    kind = args[0]
    count = int(args[1])

    if count <= 0:
        raise ValueError("Количество должно быть > 0")

    if kind == "players":
        spawn_players(count)
    elif kind == "geese":
        spawn_geese(count)
    else:
        raise ValueError("Использование: spawn players/geese <count>")

def spawn_players(count: int):
    for i in range(1, count):
        name = f"Player_{random.randint(1000, 9999)}"
        balance = random.randint(50, 500)

        try:
            casino.register_player(Player(name, balance))
        except Exception:
            pass

    typer.echo(f"Создано игроков: {count}")
def spawn_geese(count: int):
    goose_types = ["normal", "war", "honk"]

    for _ in range(count):
        gtype = random.choice(goose_types)
        name = f"Goose_{random.randint(1000, 9999)}"
        volume = random.randint(5, 30)

        try:
            if gtype == "normal":
                goose = Goose(name, volume)
            elif gtype == "war":
                goose = WarGoose(name, volume)
            else:
                goose = HonkGoose(name, volume)

            casino.register_goose(goose)

        except Exception:
            pass

    typer.echo(f"Создано гусей: {count}")

def main():
    app()


if __name__ == "__main__":
    main()
