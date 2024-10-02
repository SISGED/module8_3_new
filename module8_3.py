class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        if self.__is_valid_vin(__vin):
            self.vin_numbers = __vin
        if self.__is_valid_numbers(__numbers):
            self.numbers = __numbers

    def __is_valid_vin(self, vin_numbers):
        self.vin_numbers = vin_numbers
        if not isinstance(vin_numbers, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if self.vin_numbers < 1000000 or self.vin_numbers > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        self.numbers = numbers
        if not isinstance(self.numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(self.numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True



try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')


try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')