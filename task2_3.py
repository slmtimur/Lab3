n = int(input("Введите число: "))

fact = 1
for i in range(1, n + 1):
    fact *= i

count = 0
for i in range(fact):
    print(".", end = "")
    
    count += 1
    if count % 50 == 0:
        print("\n")
