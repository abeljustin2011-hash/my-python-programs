print("Working with Data Structures:")
print("1. Find the sum of the items in a TUPLE")
print("2. Iterate over a SET and print the values")
print("3. Print the values of a DICTIONARY of Capitals")

choice = int(input("Enter your choice: "))

def my_tuple_sum():
    my_tuple = (1, 4, 5, 7)
    total_sum = sum(my_tuple)
    print("The tuple is:", my_tuple)
    print("The sum of the items in the tuple is:", total_sum)

def iterate_set():
    my_set = {"Peach", "Mango", "Apple"}
    print("Iterating over the set:")
    for item in my_set:
        print(item)

def print_dictionary():
    capitals = {
        'Canada': 'Ottawa',
        'England': 'London',
        'Germany': 'Berlin'
    }
    print("The dictionary of capitals is:", capitals)

match choice:
    case 1:
        my_tuple_sum()
    case 2:
        iterate_set()
    case 3:
        print_dictionary()  
    case _:
        print("Wrong choice.")
    
