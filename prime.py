num = int(input("Enter a number: "))

x = 2
prime = 0

while x < num:
  if num % x == 0:
    prime = 1
    break
  x += 1

if prime == 1:
  print("It is not a prime")
else:
  print("It is a prime")
