str = "Moon"
# str[1] = "O" # immutable
print(str)

print(str.find('o')) # 1


# cruicial for parsing CSV data and user inputs.
tags = "python,java,sql"

list_tags = tags.split(",")
print(list_tags) # ['python', 'java', 'sql']

new_tags = "-".join(list_tags)  # python-java-sql
print(new_tags)


# Scenario: A user provides their email with accidental spaces and mixed cases.
# task: convert to clean lowercase without spaces.
raw_input = " User@Example.COM "
clean_email = raw_input.strip().lower()
print(clean_email)  # user@example.com



# / - float division
# // - integer division
import math
print(math.ceil(2.1)) # 3
print(math.floor(2.9)) # 2
print(math.sqrt(16)) # 4.0
print(math.factorial(5)) # 120
print(math.pi) # 3.141592653589793

# exceptional case: round() rounds to the nearest even number when the number is exactly halfway between two integers. otherwise, it rounds to the nearest integer.
print(round(3.14159, 3)) # 3.142
# print(math.pi:.3f) # mathematical operation no allowed inside (), so use f-string.
print(f"{math.pi:.3f}") # 3.142


# round(): modifies the underlying numeric value to a specified number of decimal places.
# precision formatting: controls how the number is displayed as a string, without changing its underlying value.
# round vs precision: round returns a float, while precision formatting returns a string.
prec = f"{math.pi:.3f}"
print(type(prec)) # <class 'str'>
print(type(round(math.pi, 3))) # <class 'float'>



# and or not - logical operators
# if elif else - conditional decision
# r1 if condition else r2 - ternary operator
"""
match variable:
    case expression1:
        statement1
    case expression2:
        statement2
    ....
        ....
    case _: # default case
        statement
"""



# list - mutable, ordered
# growing: .append(x), .extend(list), .insert(i, x)
# shrinking: .pop(), pop(i), .remove(x), clear()
# extra: del list[i], del list[i:j] (upto j - not included)
# order: .sort(), .reverse(), .copy()
list1 = [1, 2, 3]
list2 = list1
list3 = list1.copy() # shallow copy
list1[1] = 0
print(list2) # [1, 0, 3] - reference
print(list3) # [1, 2, 3] - no reference


# tuple - immutable, ordered
# faster than lists. used for fixed constants.
# .count(x), index(x)
# unpacking: a, b, c = (1, 2, 3)


# set - mutable, unordered collection of unique items
# .add(x), union(s), intersection(s)
# convert list to set: set1 = set(list1) 
usernames = {"Alice", "Bob", "Charlie", "Alice", "Bob"}
print(usernames) # {'Alice', 'Bob', 'Charlie'}


# dictionary - mutable, unordered collection of key-value pairs. mappable data structure and keys must be unique and immutable.
# access: dict[key], .get(key, default) - safely access keys
# .keys(), .values()
# .items() - returns a view object of key-value pairs (tuples).
# .update(dict) - Add/Update
# .pop(key) - Remove and return value
# .popitem() - Remove the last inserted item and return key-value pair



# range(start, stop, step)
# enumerate(iterable, start=i): returns an enumerate object that yields pairs of index and value from the iterable, starting from the specified index.
for i, value in enumerate(["a", "b", "c"], start=1):
    print(i, value) # 1 a, 2 b, 3 c


# while loop until a condition is met
# pass: does nothing (placeholder)
# continue: skips to the next iteration
# break: exits the loop entirely


## Extra:
# list comprehension: a concise, one-line syntax used to create a new list from an existing iterable object
# new_list = [expression for item in iterable]
numbers = [1, 2, 3, 4]
squares = [n ** 2 for n in numbers]
new_list = [n ** 2 for n in numbers if n % 2 == 0] # [4, 16]
print(squares) # [1, 4, 9, 16]
print(new_list) # [4, 16]

# conditional list comprehension
labels = ["even" if n%2 == 0 else "odd" for n in numbers]
print(labels)