# Список студентов
from typing import List


## Процедурная парадигма

# def average(student_data: List[dict[str]]) -> float:
#     return sum([i['score'] for i in student_data]) / len(student_data)

# def above_average_students(student_data: List[dict[str]], average: float) -> List[str]:
#     return [i['name'] for i in student_data if i['score'] > average]

def average(student_data: List[dict[str]]) -> float:
    total = 0
    for i in student_data:
        total += i['score']
    quantity = len(student_data)
    return total / quantity


def above_average_students(student_data: List[dict[str]], average: float) -> List[str]:
    honors_students = []
    for i in student_data:
        if i['score'] > average:
            honors_students.append(i['name'])
    return honors_students


student_data = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78},
    {'name': 'David', 'score': 95},
]

# Реализация структурной парадигмы

average1 = 0.0
above_average_students1 = []
total = 0
count = 0
for i in student_data:
    total += i['score']
    count += 1

average1 = total / count

for i in student_data:
    if i['score'] > average1:
        above_average_students1.append(i['name'])

print(f"Средний балл: {average1}")
print("Студенты с баллом выше среднего:", *above_average_students1)

print(f"Средний балл: {average(student_data)}")  # Вывод процедурной парадигмы
print("Студенты с баллом выше среднего:",
      *above_average_students(student_data, average(student_data)))  # Вывод процедурной парадигмы
