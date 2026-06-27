**Assignments3**
1)
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage:
sample_list = (8, 2, 3, 0, 7)
print("Expected Output:", sum_of_list(sample_list))

2)
def reverse_string(text):
    return text[::-1]

# Example usage:
sample_string = "1234abcd"
print("Expected Output:", reverse_string(sample_string))

3)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage:
print("Factorial of 5:", factorial(5))

4)
def count_case_letters(text):
    upper_count = 0
    lower_count = 0
    
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    print(f"No. of Upper case characters : {upper_count}")
    print(f"No. of Lower case Characters : {lower_count}")

# Example usage:
count_case_letters("Hello World")

5)
def print_even_numbers(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

# Example usage:
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Expected Result:", print_even_numbers(sample_list))

6)
def is_prime(n):
    if n <= 1:
        return False
    
    # Check for factors from 2 up to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage:
number = 11
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
