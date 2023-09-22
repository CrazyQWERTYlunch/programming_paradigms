def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Искомый элемент найден, возвращаем его индекс
        if arr[mid] < target:
            left = mid + 1  # Искомый элемент находится в правой половине
        if arr[mid] > target:
            right = mid - 1  # Искомый элемент находится в левой половине

    return -1  # Элемент не найден


def input_target():
    # Запрашиваем искомое число у пользователя
    try:
        target = int(input("Введите искомое число: "))
        return target
    except ValueError:  # Показываем ошибку и перезапускаем ввод
        print("Ошибка: Введите целое число.")
        return input_target()


# Генерируем массив
arr = [i for i in range(1, 10000000)]

target = input_target()

result = binary_search(arr, target)

if result != -1:
    print(f"Искомый элемент {target} найден в массиве по индексу {result}.")
else:
    print(f"Искомый элемент {target} не найден в массиве.")
