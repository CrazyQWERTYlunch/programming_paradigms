from random import randint, choice
from typing import List


# Задача №1. Императивный стиль
def sort_list_imperative(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[(len(numbers) + 1) // 2]
    left = list(filter(lambda x: x < pivot, numbers))
    center = [i for i in numbers if i == pivot]
    right = list(filter(lambda x: x > pivot, numbers))
    return sort_list_imperative(left) + center + sort_list_imperative(right)


# Задача №2. Декларативный стиль

def sort_list_declarative(numbers: List[int]) -> List[int]:
    return sorted(numbers)


if __name__ == '__main__':
    numbers1 = [randint(1, 100) for _ in range(50)]
    numbers2 = [randint(1, 100) for _ in range(50)]
    print(numbers1)
    print(numbers2)
    print(sort_list_imperative(numbers1))
    print(sort_list_declarative(numbers2))
