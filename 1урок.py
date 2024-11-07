# class transport:
#     def __init__(self, the_model, the_year, the_color):


class Car:
    def __init__(self, the_model, the_year, the_color):
        # self = параметры
        self.model = the_model
      # атрибут переложили в поле
        self.year = the_year
        self.color = the_color


number = 5
my_car = Car('BMW X6', '2020', 'Black')
print(my_car)
print(f'MODEL: {my_car.model} YEAR: {my_car.year} COLOR: {my_car.color}')
best_car = Car(the_year=2021, the_model='Honda FIT', the_color='Blue')
print(f'MODEL: {best_car.model} YEAR: {best_car.year} COLOR: {best_car.color}')
best_car.color = 'Red'