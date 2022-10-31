n = int(input("Введите количество элементов в массиве: "))
arr = list(map(int, input("Введите элементы массива: ").split()))

l, r = 0, 1

while True:
    flag = False
    while l != n - 1:
        if arr[l] > arr[r]:
            arr[l], arr[r] = arr[r], arr[l]
            flag = True
        l += 1
        r += 1
    if flag == False:
        break
    else:
        flag = False
        l, r = 0, 1
print(*arr)