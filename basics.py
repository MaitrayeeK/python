# comment

# print function and string concatenation
print("Hello World" + " " + "Python")

# Datatypes
#  int, float, str
#  bool, complex
#  list, tuple, set, dict

# Variables and constants
newVar = 5
first_name, last_name = "Maitrayee", "Khalasi"
boolean_value = True

# check type of variable
print(type(newVar))

# input function
number = input("Enter a number: ") # input always returns a string
print("You entered: ", number)

# Typecasting
float_number = float(number)
print("Float number: ", float_number)

# print(int(first_name)) # error

print("Maitrayee " * 2)
print(first_name[1:5])

# Objects
# Mutable: list, dict, set
# Immutable: int, float, str, tuple

# List 
my_list = [1, 2, 3, 4]
print(my_list, type(my_list))

my_list = [31, "January", 2001, "Maitrayee"]
print(my_list, type(my_list))

# Add elements
my_list.append("Khalasi")
print(my_list)

del my_list[-1]
print(my_list)

print(my_list[0:3])
print(len(my_list))

list1 = [] #empty list

# Tuple - immutable
my_tuple = (1, 2, 3, 4)
print(my_tuple, type(my_tuple))

# Set - cannot have duplicate values
# cannot support indexing
my_set = {1, 2, 3, 4}
print(my_set, type(my_set))

my_set = {1, 2, 3, 4, 4, 4}
print(my_set)

my_list = [1, 2, 3, 3, 4, 4, 4]
my_set = set(my_list)
print(my_set)

# Dictionary - key value pairs
# Can not allow duplicate keys
my_dictionary = {"fname": "Maitrayee", "lname": "Khalasi"}
print(my_dictionary, type(my_dictionary))
print(my_dictionary["fname"])
print(my_dictionary.get("lname"))

# Identity operators
# is, is not

# Membership operators
# in, not in

# Loops

for i in range(5): # 0 to 4
    print(i)

for i in my_list:
    print(i)

i = 0
while i<5:
    print(i)
    i+=1

# Functios
def my_function():
    print("Hello from function")