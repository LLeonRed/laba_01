from .errors import calculation_error


class calculator:
    # Проверка выражения на корректность и разбиение на отдельные элементы
    def vaildation(expression):
        result = []
        current = ""

        # Проверка на пустое выражение
        if not expression:
            raise calculation_error("Empty string")

        # Удаление пробелов
        expression = expression.replace(" ", "")

        # Проверка на пустое выражение после удаления пробелов
        if not expression:
            raise calculation_error("Empty string")

        # Проверка основных ошибок в структуре выражения
        valid_expression = expression.replace("*", "!").replace("//", "!").replace("/", "!")

        if (
            valid_expression.count("(") != valid_expression.count(")")
            or "!!" in valid_expression
            or valid_expression[0] == "!"
            or valid_expression[-1] in "+-!"
            or "+!" in valid_expression
            or "-!" in valid_expression
            or "+++" in valid_expression
            or "---" in valid_expression
        ):
            raise calculation_error("Incorrect expression")

        # Временная замена целочисленного деления на специальный символ
        expression = expression.replace("//", "$")

        # Добавление скобок в начало и конец выражения
        expression = "(" + expression + ")"

        # Последовательная обработка символов выражения
        for i in expression:

            # Проверка допустимых символов
            if i not in "0123456789+-*/().$":
                raise calculation_error("Unknown symbol")

            # Обработка скобок
            if i in "()":
                if current:
                    if len(current) > 1 and current[0] == "0":
                        raise calculation_error("Incorrect expression")

                    result.append(current)
                    current = ""

                if i == "(":
                    if result and result[-1] == ")":
                        raise calculation_error("Incorrect expression")

                    if result and result[-1] not in "(+-*/$":
                        raise calculation_error("Incorrect expression")

                if i == ")" and (not result or result[-1] in "(+-*/$"):
                    raise calculation_error("Incorrect expression")

                result.append(i)

            else:
                # Добавление символа к текущему элементу
                current += i

                # Обработка операторов и унарных знаков
                if (
                    (not result or result[-1] in "(*-+$/")
                    and current[0] in "+-*/$"
                    and len(current) > 1
                ):
                    if current[0] in "+-" and current[-1] in "+-*/":

                        if len(current[:-1]) > 1 and current[:-1][0] == "0":
                            raise calculation_error("Incorrect expression")

                        result.append(current[:-1])
                        current = current[-1]

                elif len(current) > 1:

                    # Отделение оператора от начала элемента
                    if current[0] in "+-*/$":
                        result.append(current[0])
                        current = current[1:]

                    # Отделение оператора от конца элемента
                    elif current[-1] in "+-*/$":

                        if len(current[:-1]) > 1 and current[:-1][0] == "0":
                            raise calculation_error("Incorrect expression")

                        result.append(current[:-1])
                        current = current[-1]

        return result[1:-1]

    # Преобразование выражения в обратную польскую запись
    def tokenization(expression):

        expression = [i if i != "$" else "//" for i in expression]

        order = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "//": 2,
        }

        result = []
        stack = []
        number = ""

        for i in expression:

            if i not in "+-*//()":
                number += i

            elif i in "+-*//":

                if number:
                    result.append(number)
                    number = ""

                while stack and order[stack[-1]] >= order[i]:
                    result.append(stack[-1])
                    stack.pop(-1)

                stack.append(i)

            elif i == "(":
                if number:
                    result.append(number)
                    number = ""

                stack.append("(")

            elif i == ")":
                if number:
                    result.append(number)
                    number = ""

                while stack and stack[-1] != "(":
                    result.append(stack[-1])
                    stack.pop(-1)

                stack.pop(-1)

        if number:
            result.append(number)

        for j in stack[::-1]:
            result.append(j)

        return result

    # Вычисление выражения в обратной польской записи
    def calculation(expression):
        index = 0

        while len(expression) > 1:

            if expression[index] not in "+-*//":
                index += 1

            else:
                insertable = ""

                if expression[index] == "+":
                    insertable = float(expression[index - 2]) + float(expression[index - 1])

                elif expression[index] == "-":
                    insertable = float(expression[index - 2]) - float(expression[index - 1])

                elif expression[index] == "*":
                    insertable = float(expression[index - 2]) * float(expression[index - 1])

                else:
                    if float(expression[index - 1]) == 0:
                        raise calculation_error("Zero division")

                    if expression[index] == "/":
                        insertable = float(expression[index - 2]) / float(expression[index - 1])
                    else:
                        insertable = float(expression[index - 2]) // float(expression[index - 1])

                expression.insert(index - 2, str(insertable))
                index = index - 2

                for i in range(3):
                    expression.pop(index + 1)

        return expression[0]

    # Последовательное выполнение всех этапов обработки выражения
    def evaluate(expression):
        return float(
            calculator.calculation(
                calculator.tokenization(
                    calculator.vaildation(expression)
                )
            )
        )
