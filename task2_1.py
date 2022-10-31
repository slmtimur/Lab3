n = int(input("Введите количество элементов: "))
arr = list(map(int, input("Введите элементы через пробел: ").split()))

min_n = arr[0]
max_n = arr[0]
sredn = 0

for i in arr:
    if i > max_n:
        max_n = i
for i in arr:
    if i < min_n:
        min_n = i
for i in arr:
    sredn += i

print("\nМинимальный элемент - ", min_n)
print("Максимальный элемент - ", max_n)
print("Среднее арифметическое - ", sredn / n)