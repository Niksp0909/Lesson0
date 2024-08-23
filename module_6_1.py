class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def __str__(self):
        return self.name

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

    def __str__(self):
        return self.name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

# Пример выполнения программы
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)  # Вывод: Волк с Уолл-Стрит
print(p1.name)  # Вывод: Цветик семицветик

print(a1.alive)  # Вывод: True
print(a2.fed)    # Вывод: False

a1.eat(p1)  # Вывод: Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)  # Вывод: Хатико съел Заводной апельсин

print(a1.alive)  # Вывод: False
print(a2.fed)    # Вывод: True
