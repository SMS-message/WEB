def ex1() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("arg1")
    parser.add_argument("arg2", nargs="+")
    args = parser.parse_args()
    print(args.arg1, args.arg2)

def ex2() -> None:
    import argparse
    import sys
    parser = argparse.ArgumentParser()

    parser.add_argument("args", metavar="Целые числа", nargs="+",
                        type=str, help="Перевод двоичных чисел в десятичные")
    parser.add_argument("--base", metavar="Основание системы счисления", default=2,
                        type=int, help="Основание системы счисления")
    parser.add_argument("--log", default=sys.stdout, metavar="Файл для логирования",
                        type=argparse.FileType('a'), help="Файл для логирования")

    args = parser.parse_args()

    result = list(map(lambda x: str(int(x, args.base)), args.args))
    args.log.write(" ".join(result) + '\n')
    args.log.close()

def ex3() -> None:
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("--name")
    parser.add_argument("-up", "--up_case", action="store_true",
                        help="Перевод имени в верхний регистр")
    parser.add_argument("--number", choices=[0, 1, 2], type=int, default=0,
                        help="Выбор номера", required=True)
    parser.add_argument("--no-name", action="store_const", const="no", dest="name")

    args = parser.parse_args()
    name: str = args.name
    if args.up_case:
        name = name.upper()
    print(f"Наше имя: {name}. И наш номер: {args.number}")

def main() -> None:
    ex3()

if __name__ == '__main__':
    main()