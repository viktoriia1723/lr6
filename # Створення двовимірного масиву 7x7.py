# Створення двовимірного масиву 7x7
array = [[0 for _ in range(7)] for _ in range(7)]

# Заповнення масиву за вказаним шаблоном
for i in range(7):
    for j in range(7):
        array[i][j] = (i + j) % 2

# Виведення масиву на екран
for row in array:
    for element in row:
        print(element, end=" ")
    print()  # Перехід на новий рядок після кожного рядка масиву