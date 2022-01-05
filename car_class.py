# https://python-scripts.com/object-oriented-programming-in-python

class Car:

    name = "c200"
    make = "mercedez"
    model = 2008

    def start(self):
        print("Заводим двигатель")

    def stop(self):
        print("Отключаем двигатель")


car_a = Car()
car_b = Car()

print(type(car_a))
print(car_a.start())
print(dir(car_b))

class Car:
    # атрибут класса
    car_count = 0

    def start(self, name, make, model):
        print("Двигатель заведен")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1


car_a = Car()
car_a.start("Corolla", "Toyota", 2015)
print(car_a.name)
print(car_a.car_count)

car_b = Car()
car_b.start("City", "Honda", 2013)
print(car_b.name)
print(car_b.car_count)

class Car:

    @staticmethod
    def get_class_details():
        print("Это класс Car")


Car.get_class_details()


class Square:

    @staticmethod
    def get_squares(a,b):
        return a*a, b*b


print(Square.get_squares(3, 5))


class Car:

    def __str__(self):
        return "Car class Object"

    def start(self):
        print("Двигатель заведен")


car_a = Car()
print(car_a)

class Car:

    car_count = 0

    def __init__(self):
        Car.car_count += 1
        print(Car.car_count)

car_a = Car()
car_b = Car()
car_c = Car()

class Car:
    message1 = "Двигатель заведен"

    def start(self):
        message2 = "Автомобиль заведен"
        return message2

car_a = Car()
print(car_a.message1)


class Car:
    def __init__(self):
        print("Двигатель заведен")
        self.name = "corolla"
        self.__make = "toyota"
        self._model = 1999


car_a = Car()
print(car_a.name)

# Наследование
class Vehicle:
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")


class Car(Vehicle):
    def car_method(self):
        print("Это метод из дочернего класса")


class Cycle(Vehicle):
    def cycleMethod(self):
        print("Это дочерний метод из класса Cycle")


car_a = Car()
car_a.vehicle_method()
car_b = Cycle()
car_b.vehicle_method()


class Camera:
    def camera_method(self):
        print("Это родительский метод из класса Camera")


class Radio:
    def radio_method(self):
        print("Это родительский метод из класса Radio")


class CellPhone(Camera, Radio):
    def cell_phone_method(self):
        print("Это дочерний метод из класса CellPhone")


cell_prone_a = CellPhone()
cell_prone_a.camera_method()
cell_prone_a.radio_method()


# Полиморфизм
class Car:
    def start(self, a, b=None):
        if b is not None:
            print(a + b)
        else:
            print(a)


car_a = Car()
car_a.start(10)
car_a.start(10, 20)


# Инкапсуляция

class Car:
    # инициализируем свойства (определяем атрибут)
    def __init__(self, model):
        self.model = model

    # создаем свойство модели (определяем свойство атрибута)
    @property
    def model(self):
        return self.__model

    # сеттер для создания свойств (установщик свойства)
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model == model

    def getCarModel(self):
        return "Год выпуска модели " + str(self.model)


car_a = Car(2088)
print(car_a.getCarModel())
