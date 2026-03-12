low = int(input("Enter the lower range: "))
high = int(input("Enter the higher range: "))

divisor = 2

for prime in (low, high):
    if prime % divisor == 0:
        print(prime)
    divisor += 1
