import random 

def start_program():
    print("Program Menu")
    print(" 1. Random selection from a given list")
    print(" 2. Random selection of a number")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item_list = [1, 'd', 'a', 32, 3.14, 'hello']
        random_item = random.choice(item_list)
        print("The list is:", item_list)
        print("Randomly selected item:", random_item)
    elif choice == 2:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        random_number = random.randint(start, end)
        print("Randomly selected number:", random_number)
    else:
        print("Wrong choice.")
        start_program()
    
start_program()
