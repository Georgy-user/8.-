class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model  # Название автомобиля (строка).
        if self.__is_valid_vin(vin):
            self.__vin = vin  # Vin номер автомобиля (целое число).
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers  # Номера автомобиля (строка).

    def __is_valid_vin(self, vin_numbers):  # Проверка vin_number на корректность.
        if not isinstance(vin_numbers, int):
            raise IncorrectVinNumber('Некорректный тип vin номер.')
        elif vin_numbers > 9999999 or vin_numbers < 1000000:
            raise IncorrectVinNumber('Неверный диапазон для vin номера.')
        else:
            return True

    def __is_valid_numbers(self, numbers):  # Проверка numbers на корректность.
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров.')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера.')
        else:
            True


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
