# Была выбрана процедурная парадигма по причине большей гибкости,
# простоты дальнейшего расширения и переиспользования с парой значений

def multiply_table(multiplier: int, multipliable: int = 1) -> None:
    """Выводит на экран таблицу умножения всех чисел от 1 до n
    :param multiplier: int
    :param multipliable: int """

    # Отрисовка таблицы умножения
    for i in range(1, multiplier + 1):
        print(f'{multipliable} * {i} = {multipliable * i}')


# ввод значения
n = int(input())
# вызов функции multiply_table с переданным в неё аргументом n
multiply_table(n)
