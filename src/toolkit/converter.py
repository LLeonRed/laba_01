from .errors import convertation_error
import string


class converter:
    # Коэффициенты перевода единиц массы в граммы
    weight = {
        "g": 1,
        "kg": 10**3
    }

    # Коэффициенты и смещения для перевода температур
    temperature = {
        "c": [1, 0],
        "k": [1, 273.15],
        "f": [1.8, 32]
    }

    # Коэффициенты перевода единиц длины в сантиметры
    length = {
        "mm": 10**-1,
        "cm": 1,
        "m": 10**2,
        "km": 10**5
    }

    # Проверка входных данных и выполнение конвертации
    def verification(value, frm, to):

        # Проверка значения на допустимые символы
        for k in str(value):
            if k not in "0123456789.":
                raise convertation_error("Invalid value")

        # Приведение исходной единицы измерения к нижнему регистру
        fixed_from = ""
        fixed_to = ""

        for j in frm:
            if j in string.ascii_uppercase:
                index = string.ascii_uppercase.index(j)
                fixed_from += string.ascii_lowercase[index]
            else:
                fixed_from += j

        # Приведение конечной единицы измерения к нижнему регистру
        for j in to:
            if j in string.ascii_uppercase:
                index = string.ascii_uppercase.index(j)
                fixed_to += string.ascii_lowercase[index]
            else:
                fixed_to += j

        # Проверка принадлежности единиц к группам
        check_weight = (fixed_from in converter.weight) + (fixed_to in converter.weight)
        check_length = (fixed_from in converter.length) + (fixed_to in converter.length)
        check_temperature = (fixed_from in converter.temperature) + (fixed_to in converter.temperature)

        # Проверка неизвестных единиц измерения
        if check_weight + check_length + check_temperature < 2:
            raise convertation_error("Unknown unit")

        # Проверка попытки перевода между разными группами единиц
        elif 0 < check_weight < 2 or 0 < check_length < 2 or 0 < check_temperature < 2:
            raise convertation_error("Inconvertable units")

        # Конвертация единиц массы
        if check_weight == 2:
            return value * converter.weight[fixed_from] / converter.weight[fixed_to]

        # Конвертация единиц длины
        elif check_length == 2:
            return value * converter.length[fixed_from] / converter.length[fixed_to]

        # Конвертация температуры
        else:
            if fixed_from == "f":
                value_temp = (
                    value - converter.temperature[fixed_from][1]
                ) / converter.temperature[fixed_from][0]
            else:
                value_temp = (
                    value - converter.temperature[fixed_from][1]
                ) * converter.temperature[fixed_from][0]

            # Проверка температуры ниже абсолютного нуля
            if value_temp < -273.15:
                raise convertation_error("Below zero")

            else:
                if fixed_to == "f":
                    return (
                        value_temp * converter.temperature[fixed_to][0]
                        + converter.temperature[fixed_to][1]
                    )
                else:
                    return (
                        value_temp * converter.temperature[fixed_to][0]
                        + converter.temperature[fixed_to][1]
                    )

