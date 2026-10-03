import argparse

from toolkit.calculator import calculator
from toolkit.converter import converter


parse = argparse.ArgumentParser(
    description="CLI-набор утилит: калькулятор выражений и конвертер единиц"
)

subparse = parse.add_subparsers(
    dest="command",
    required=True
)


calc_parser = subparse.add_parser(
    "calc",
    help="Вычислить математическое выражение.",
    description="Вычисляет математическое выражение с операциями +, -, *, / и скобками"
)

calc_parser.add_argument(
    "expression",
    help='Математическое выражение, например: "2 + 3 * 4"'
)


convert_parser = subparse.add_parser(
    "convert",
    help="Конвертировать значение между единицами измерения",
    description="Конвертирует длину, массу или температуру между поддерживаемыми единицами"
)

convert_parser.add_argument(
    "value",
    type=float,
    help="Числовое значение для конвертации"
)

convert_parser.add_argument(
    "--from",
    dest="from_unit",
    required=True,
    type=str,
    help="Исходная единица измерения"
)

convert_parser.add_argument(
    "--to",
    dest="to_unit",
    required=True,
    type=str,
    help="Целевая единица измерения"
)


args = parse.parse_args()


if args.command == "calc":
    print(float(calculator.evaluate(args.expression)))

elif args.command == "convert":
    print(float(converter.verification(args.value, args.from_unit, args.to_unit)))

else:
    print("Unknown command")
