def bin_poisk(arr, n, f):
    arr.sort()
    l, r = -1, n
    while l != r - 1:
        ind = (l + r) // 2
        if arr[ind] == f:
            return True
        else:
            if arr[ind] < f:
                l = ind
            else:
                r = ind

    return False


a, b, c = map(int, input("Введите три числа через пробел: ").split())

n = int(input("Введите количество элементов в массивах: "))
arr1 = list(map(int, input("Введите элементы первого массива: ").split()))
arr2 = list(map(int, input("Введите элементы второго массива: ").split()))
arr3 = list(map(int, input("Введите элементы третьего массива: ").split()))

if bin_poisk(arr1, n, a):
    print("\nЧисло a находится в первом массиве")
else:
    print("Число a не находится в первом массиве")

if bin_poisk(arr2, n, b):
    print("Число b находится во втором массиве")
else:
    print("Число b не находится во втором массиве")

if bin_poisk(arr3, n, c):
    print("Число с находится в третьем массиве")
else:
    print("Число c не находится в третьем массиве")
