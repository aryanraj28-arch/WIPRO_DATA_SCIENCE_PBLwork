**Assignments**
1)# Create a list of 5 integers
my_list = [10, 20, 30, 40, 50]

# Display the list items
print("Full list:", my_list)

# Access individual elements through index
print("Element at index 0:", my_list[0])
print("Element at index 2:", my_list[2])
print("Element at index 4:", my_list[4])

2)
my_list = [10, 20, 30, 40, 50]

# Append a new item to the end of the list
my_list.append(60)

print("List after appending:", my_list)

3)
my_list = [10, 20, 30, 40, 50]

# Reverse the list in place
my_list.reverse()

print("Reversed list:", my_list)

4)
my_list = [10, 20, 30, 20, 40, 20, 50]
specified_element = 20

# Get the number of occurrences
occurrences = my_list.count(specified_element)

print(f"The element {specified_element} appears {occurrences} times.")

5)
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Append list1 items to the front of list2
result = list1 + list2

print("Combined list (list1 at the front):", result)

6)
my_list = [10, 20, 30, 40]

# Index 1 is the position of the second element, so inserting there shifts it right
my_list.insert(1, 15)

print("List after insertion:", my_list)

7)'
my_list = [10, 20, 30, 40, 50]
target_index = 2

# Remove item from the specified index using pop()
removed_item = my_list.pop(target_index)

print(f"Removed item '{removed_item}' from index {target_index}.")
print("Updated list:", my_list)

8)
my_list = [10, 20, 30, 20, 40]
element_to_remove = 20

# Remove the first occurrence of the specified element
my_list.remove(element_to_remove)

print("List after removing the first occurrence:", my_list)

9)
# Initial dictionary
sample_dict = {0: 10, 1: 20}

# Adding a new key-value pair
sample_dict[2] = 30

print("Updated Dictionary:", sample_dict)

10)
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create a new dictionary and update it with all others
expected_result = {}
expected_result.update(dic1)
expected_result.update(dic2)
expected_result.update(dic3)

print("Concatenated Dictionary:", expected_result)

11)
my_dict = {1: 10, 2: 20, 3: 30}
key_to_check = 2

# Check existence using the 'in' keyword
if key_to_check in my_dict:
    print(f"Key {key_to_check} exists in the dictionary.")
else:
    print(f"Key {key_to_check} does not exist in the dictionary.")

12)
my_dict = {'a': 100, 'b': 200, 'c': 300}

# 1. Printing keys alone
print("Keys:")
for key in my_dict.keys():
    print(key, end=" ")
print("\n")

# 2. Printing values alone
print("Values:")
for value in my_dict.values():
    print(value, end=" ")
print("\n")

# 3. Printing both keys and values
print("Keys and Values:")
for key, value in my_dict.items():
    print(f"{key} -> {value}")
13)
# Generate dictionary using a loop (or dict comprehension)
squares_dict = {}
for x in range(1, 16):
    squares_dict[x] = x ** 2

print("Squares Dictionary:")
print(squares_dict)

14)
my_dict = {'item1': 50, 'item2': 150, 'item3': 200}

# Summing values using the built-in sum() function
total_sum = sum(my_dict.values())

print("Sum of all values:", total_sum)

15)
# Sample tuple with at least 4 elements
my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)

# Positive indexing starts at 0, so the 4th element is at index 3
fourth_from_start = my_tuple[3]

# Negative indexing starts at -1, so the 4th element from last is at index -4
fourth_from_last = my_tuple[-4]

print("4th element from first:", fourth_from_start)
print("4th element from last:", fourth_from_last)

16)
my_tuple = ('a', 'b', 'c', 'd', 'e')
search_element = 'c'

# Check existence using the 'in' keyword
if search_element in my_tuple:
    print(f"Element '{search_element}' exists in the tuple.")
else:
    print(f"Element '{search_element}' does not exist in the tuple.")
17)
# Sample list
my_list = [1, 2, 3, 4, 5]

# Convert using the built-in tuple() constructor
my_tuple = tuple(my_list)

print("Converted tuple:", my_tuple)
print("Type:", type(my_tuple))

18)
# Sample list
my_list = [1, 2, 3, 4, 5]

# Convert using the built-in tuple() constructor
my_tuple = tuple(my_list)

print("Converted tuple:", my_tuple)
print("Type:", type(my_tuple))

19)
my_tuple = (10, 20, 30, 40, 50)
item_to_find = 30

# Find index using the index() method
index_position = my_tuple.index(item_to_find)

print(f"The index of {item_to_find} is: {index_position}")

20)
# Sample input list containing tuples
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# Since tuples are immutable, we convert each tuple to a list, 
# modify the last element, and convert it back to a tuple.
expected_output = []
for t in sample_list:
    modified_list = list(t)
    modified_list[-1] = 100
    expected_output.append(tuple(modified_list))

print("Expected Output:", expected_output)

21)
# Sample set
my_set = {10, 20, 30, 40, 50}
item_to_remove = 30

# Using discard() is safer than remove() as it won't raise an error if the item doesn't exist
my_set.discard(item_to_remove)

print("Set after removing item:", my_set)

22)
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Find common elements using the intersection() method or & operator
intersection_set = set_a.intersection(set_b)

print("Intersection of sets:", intersection_set)

23)
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Combine all unique elements using the union() method or | operator
union_set = set_a.union(set_b)

print("Union of sets:", union_set)

24)
my_set = {5, 2, 9, 11, 4, 7}

# Find max and min using built-in functions
max_value = max(my_set)
min_value = min(my_set)

print("Maximum value:", max_value)
print("Minimum value:", min_value)

25)
def count_case(input_string):
    upper_count = 0
    lower_count = 0
    
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    print(f"Uppercase letters: {upper_count}")
    print(f"Lowercase letters: {lower_count}")

# Example usage:
count_case("Hello World!")

26)
def is_palindrome(input_string):
    # Normalize string by removing spaces and converting to lowercase
    cleaned_string = "".join(input_string.split()).lower()
    
    # Check if the string matches its reverse
    if cleaned_string == cleaned_string[::-1]:
        print(f"'{input_string}' is a Palindrome.")
    else:
        print(f"'{input_string}' is not a Palindrome.")

# Example usage:
is_palindrome("Radar")
27)

def copy_chars(input_string):
    n = len(input_string)
    if n >= 2:
        # Get first 2 characters and multiply by the length of the string
        result = input_string[:2] * n
        return result
    else:
        return "String length must be >= 2"

# Example usage:
print(copy_chars("Wipro"))  # Output: WiWiWiWiWi
 28)
def repeat_last_n(input_string, n):
    # Slice the last n characters
    last_n_chars = input_string[-n:] if n > 0 else ""
    # Repeat it n times
    return last_n_chars * n

# Example usage:
print(repeat_last_n("Wipro", 3))  # Output: propropro