low = int(input("Enter the lower range: "))
high = int(input("Enter the higher range: "))

for num in range(low, high):
    x = 2
    prime = 1
    while x < num:
        if num % x == 0:
            prime = 0
            break
        x += 1
    if prime == 1:
        print(num)
