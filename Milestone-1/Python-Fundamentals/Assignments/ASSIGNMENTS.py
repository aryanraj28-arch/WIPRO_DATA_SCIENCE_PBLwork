ASSIGNMENTS**
**FLOW CONTROL STATEMENTS**
-->1)
num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
-->2)
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
-->3)
def lastDigit(a, b):
    return a % 10 == b % 10

print(lastDigit(7, 17))    # True
print(lastDigit(6, 17))    # False
print(lastDigit(3, 113))   # True
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 10 == num2 % 10:
    print(True)
else:
    print(False)
--> 4)
for i in range(1, 11):
    print(i, end="\t")

--> 5)
for i in range(23, 58):
    if i % 2 == 0:
        print(i)
-->6)
num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime")

--> 7)
for num in range(10, 100):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)

--8)
num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print("Sum of digits =", sum_digits)

-->9) 
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse number =", reverse)

-->10)
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
