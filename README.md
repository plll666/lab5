# Лабораторная работа №4  
## Казино и Гуси — симуляция с пользовательскими коллекциями

Проект реализует симуляцию казино, в которой участвуют:
- игроки,
- гуси (обычные, боевые и кричащие),
- фишки казино.

В работе используются:
- пользовательские коллекции (списковая и словарная),
- наследование,
- магические методы,
- псевдослучайная модель с возможностью фиксировать seed.

---

## Структура проекта

src/  
│ ├── init.py  
│ ├── main.py  
│ ├── casino/  
│ │ ├── init.py  
│ │ ├── casino.py   
│ │ ├── casino_balance.py  
│ │ └── chip.py   
│ ├── players/  
│ │ ├── init.py  
│ │ ├── player.py    
│ │ └── player_collection.py   
│ └── gooses/  
│ ├── init.py  
│ ├── Goose.py   
│ └── goose_collection.py  
├── tests/  
│ ├── init.py  
│ ├── test_casino_balance.py   
│ ├── test_chip.py   
│ ├── test_goose_collection.py  
│ ├── test_goose_exceptions.py  
│ ├── test_goose_magic.py  
│ ├── test_player_collection.py  
│ ├── test_player_exceptions.py  
│ └── test_simulation_seed.py  
├── README.md  
├── .gitignore   
├── .pre-commit-config.yaml   
└── uv.lock   

---

## Основные компоненты

### Player  
Игрок с именем и балансом.

### Goose, WarGoose, HonkGoose  
- Goose — базовый гусь  
- WarGoose — атакует игроков  
- HonkGoose — изменяет балансы игроков (реализует `__call__`)  
- Поддерживается объединение гусей через `__add__`

### Chip  
Фишка казино.  
Поддерживает `__add__` и `__radd__` (Chip + Chip, Chip + int).

### PlayerCollection / GooseCollection  
Пользовательские списковые коллекции:
- поддерживают индексацию,
- срезы,
- итерацию,
- удаление по объекту и по имени,
- поиск.

### CasinoBalance  
Пользовательская словарная коллекция, логирующая изменения балансов.

---

## Симуляция

Метод:

```
casino.run_simulation(steps, seed=None)
```
На каждом шаге случайно выбирается одно событие:
- ставка игрока
- выигрыш
- атака боевого гуся
- крик HonkGoose
- попытка кражи
- объединение гусей
- паника игрока

При передаче `seed` симуляция становится воспроизводимой.

## Запуск 

```python -m src/main.py```

## Тестирование

Тесты проверяют:
- коллекции
- магические методы
- поведение событий
- работу seed

## Запуск:

```pytest -v```