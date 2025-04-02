print("Hello World")

# Variable creation
# x = 5
# y = "Hello"
# print(x,y)

x = 5
y = "Hello"
print(x,y)

# Variable types
#  PY - Number, Strings, Boolean, Objects, List, Tuple, Dictinary
list = [1, 2, 3, 4, 5]
print(list)
#  add 6 to the list
list.remove(1)
print(list)
# remove last element from list
list.pop()
print(list)
# remove all elements from the list
list.clear()
print(list)
# create a dictionary
#  dict = {key: value}
dict = {"name": "John", "age": 30, "city": "New York"}
print(dict)
#  add a key to the dictionary
dict["country"] = "USA"
print(dict)
#  remove a key from the dictionary
dict.pop("name")
print(dict)
dict.clear()
print(dict)

# for loop
for i in range(5):
    print(i)
    
# while loop
i = 0
while i <= 5:
    print(i)
    i += 1

# if else statement
x = 5
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero") 

# function creation
def add(a, b):
    return a + b     
print(add(5, 10))

#  create an input from the user
name = input("Enter your name:")
print("Hello" + name)

number = input("Enter a number:")
print("The number is" + number)

number = float(input("Enter a number:"))
print("The number is" + str(number))

#  Mini Challenge -- Create a Calculator that takes two numbers
#  use this operators (+, -, *, /) and returns the results.


# fucntion
def print_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
print_menu()

# take input from the user
choice = input("Enter choice:")
num1 = float(float("Enter first number:"))
num2 = float(float("Enter second number:"))
result = 0
if choice == "1":
    result = num1 + num2
elif choice == "2":
    result = num1 + num2
elif choice == "3":
    result = num1 + num2
elif choice == "4": 
    if num2 == 0:
        print("cannout divide by zero")
        exit(1)
    else:
        result = num1 / num2
elif choice == "S":
    print("Exiting...") 
else:
    print("Invalid choice")
    exit(1)
print("Result: ", result)                            
