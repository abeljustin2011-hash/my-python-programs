sandwiches = ["Chicken Sandwich","Beef Sandwich","Tofu Sandwich"]

sandwich_prices = {
  "Chicken Sandwich":5.25,
  "Beef Sandwich": 6.25,
  "Tofu Sandwich":5.75,
}

sizes = ["small","medium","large"]

drink_prices = {
  "small":1.00,
  "medium": 1.75,
  "large":2.25,
}

fries_prices = {
  "small":1.00,
  "medium": 1.50,
  "large":2.00,
}

total_price = 0
discount = 0

for index, value in enumerate(sandwiches, start=1):
  print(f" {index}. {value} ${sandwich_prices[value]}")
user_sandwich = int(input("Choose an option: "))
print("You chose the", sandwiches[user_sandwich - 1])

total_price = sandwich_prices[sandwiches[user_sandwich - 1]]

drink_choice = input("Would you like a beverage (Yes or No): ")
if drink_choice == "Yes":
  for index, value in enumerate(sizes, start=1):
    print(f" {index}. {value} ${drink_prices[value]}")
  user_drink = int(input("Choose an option: "))
  print("You chose the", sizes[user_drink - 1],"drink")
  total_price = total_price + drink_prices[sizes[user_drink - 1]]
  
fries_choice = input("Would you like fries (Yes or No): ")
if fries_choice == "Yes":
  for index, value in enumerate(sizes, start=1):
    print(f" {index}. {value} ${fries_prices[value]}")
  user_fries = int(input("Choose an option: "))
  print("You chose the", sizes[user_fries - 1],"fries")
  if sizes[user_fries - 1] == "small":
    is_mega_size = input("Would you like to mega-size your fries (Yes, No): ")
    if is_mega_size == "Yes":
      user_fries = 3
  total_price = total_price + fries_prices[sizes[user_fries - 1]]

ketchup_choice = int(input("How many ketchup packets would you like to order?: "))

total_price = total_price + (ketchup_choice * 0.25)
if drink_choice == "Yes" and fries_choice == "Yes":
  discount = 1
  total_price = total_price - discount
print("Your order today: ")
print(sandwiches[user_sandwich - 1],"$", sandwich_prices[sandwiches[user_sandwich - 1]])
if drink_choice == "Yes":
  print(sizes[user_drink - 1],"drink","$", drink_prices[sizes[user_drink - 1]])
if fries_choice == "Yes":
  print(sizes[user_fries - 1],"fries","$", fries_prices[sizes[user_fries - 1]])
print(ketchup_choice, "ketchup packets","$", (ketchup_choice * 0.25))
if discount:
  print("Your discount today is $1")
print("The cost of your meal is: $",total_price)
print("The cost of my meal is: $",total_price)













