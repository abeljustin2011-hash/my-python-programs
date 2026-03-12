list = [10, 54, 31, 49, 51, 68]
print("The list of numbers:", list)

def even_sum(list):
    final = 0
    for num in list:
        if num % 2 == 0:
            final += num
    return final

print("The sum of even numbers is:", even_sum(list))