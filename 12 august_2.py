# Создаем базовый список
numbers = [1, 2, 3]

# Вставляем число 4 на позицию с индексом 1
numbers.insert(1, 4)

print("Результирующий список:", numbers)

name = input()
print("Привет,", name)

while True:
    name = input()
    print("Привет,", name)

# Вариант 1: через два print()
print("Привет")
print("Мир")

# Вариант 2: через один print() и символ \n
print("Привет\nМир")