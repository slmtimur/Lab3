n = int(input("Введите количество элементов: "))
arr = list(map(int, input("Введите элементы через пробел: ").split()))


for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] < 10 and arr[j] < 10 and arr[k] < 10 and arr[i] != 0:
                print(str(arr[i]) + str(arr[j]) + str(arr[k]))