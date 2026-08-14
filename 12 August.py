# 1. Изменение исходного объекта через вторую ссылку
x = [1, 2, 3]
y = x
y.append(4)  # Добавляем 4 в конец списка

print("Сценарий с одной ссылкой:")
print("x:", x)
print("y:", y)

# 2. Изменение независимой копии
a = [1, 2, 3]
b = a.copy()  # Создаем ОТДЕЛЬНЫЙ список в памяти
b.append(4)

print("\nСценарий с копией:")
print("a:", a)
print("b:", b)

# Вариант 1: через два print()
print("Привет")
print("Мир")

# Вариант 2: через один print() и символ \n
print("Привет\nМир")
print("A\n\nB")

delimiter = '/'
print('a', 'b', sep=delimiter, end='+')
print('c', 'd', sep='*', end=delimiter)
