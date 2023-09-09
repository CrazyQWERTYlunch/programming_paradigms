# Задача-2: У вас есть массив, содержащий числа от 1 до N, где N - длина массива.
# Одно из чисел в массиве повторяется дважды, а одно число пропущено. Найдите повторяющееся число и пропущенное число.

lst = list(map(int, input().split()))

for i, j in enumerate(sorted(lst), 1):
    if i != j:
        print("Повторяющееся число:", j)
        print("Пропущено число", i)