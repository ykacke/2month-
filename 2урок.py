class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        return f'NAME: {self.name}, AGE: {self.age}, BIRTH DAY: {2024 - self.age}'


some_animal = animal('anim', 3)
some_animal.age = 'Five years old'


print(animal)