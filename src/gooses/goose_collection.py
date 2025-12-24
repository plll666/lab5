from src.gooses.Goose import Goose, WarGoose, HonkGoose

class GooseCollection:
    def __init__(self, gooses=[]):
        self._gooses = gooses

    def add(self, goose: Goose):
        if not isinstance(goose, (Goose, WarGoose, HonkGoose)):
            raise TypeError(f"{goose} должен быть гусем")

        if goose in self._gooses:
            raise ValueError(f"Гусь с именем '{goose.name}' уже существует")

        self._gooses.append(goose)
        print(f"Гусь '{goose.name}' добавлен")

    def remove(self, goose):
        if isinstance(goose, (Goose, WarGoose, HonkGoose)):
            if goose not in self._gooses:
                raise ValueError("Гусь не найден")
            self._gooses.remove(goose)
            print(f"Удалён гусь: {goose.name}")
            return goose

        elif isinstance(goose, str):
            for g in self._gooses:
                if g.name == goose:
                    self._gooses.remove(g)
                    print(f"Удалён гусь: {g.name}")
                    return g
            raise ValueError("Гусь с таким именем не найден")

        else:
            raise TypeError("remove принимает Goose или имя")

    def __len__(self):
        return len(self._gooses)

    def __iter__(self):
        return iter(self._gooses)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return GooseCollection(self._gooses[index])
        return self._gooses[index]

    def __contains__(self, item):
        if isinstance(item, (Goose, WarGoose, HonkGoose)):
            return item in self._gooses
        if isinstance(item, str):
            return any(g.name == item for g in self._gooses)
        return False

    def find_by_name(self, name):
        for g in self._gooses:
            if g.name == name:
                return g
        return None

    def find_by_type(self, goose_type):
        """Поиск гусей по типу"""
        result = GooseCollection()
        for g in self._gooses:
            if isinstance(g, goose_type):
                result.add(g)
        return result