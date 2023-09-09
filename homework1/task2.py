# Задача- 1: У вас есть массив целых чисел, в котором каждое число, кроме одного, повторяется дважды.
# Вам нужно найти это одиночное число.
from typing import List


def declarative_find(lst: List[int]) -> int | None:
    for i in lst:
        if lst.count(i) == 1:
            return i
    return None


def imperative_find(lst: List[int]) -> int | None:
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            if lst[i] == lst[j]:
                break
        else:
            return lst[i]
    return None


# lst = [1, 2, 3, 4, 5, 4, 3, 2, 1] # массив для быстрой проверки

lst = list(map(int, input().split()))

print(declarative_find(lst))
print(imperative_find(lst))

