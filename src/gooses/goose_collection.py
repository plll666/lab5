from src.gooses.Goose import Goose

class GooseCollection:
    def __init__(self):
        self._gooses = []

    def __len__(self):
        return len(self._gooses)
    def __getitem__(self, item):
        return self._gooses[item]
    def __iter__(self):
        return iter(self._gooses)

    def add(self, goose: Goose):
        if not isinstance(goose, Goose):
            raise TypeError(f"{goose} должен быть гусем")

        if goose in self._gooses:
            raise ValueError(f"Гусь с именем '{goose.name}' уже существует")

        self._gooses.append(goose)
        print(f"Гусь '{goose.name}' добавлен")

    def remove(self, goose):
        if isinstance(goose, Goose):
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



