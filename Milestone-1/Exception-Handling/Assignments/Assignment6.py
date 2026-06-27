**Assignment6**
1)
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid integers.")
2)
try:
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

except ValueError:
    print("Error: Please enter a valid number.")

3)

try:
    filename = input("Enter file name: ")

    file = open(filename, "r")

    content = file.read()

    print(content.title())

    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")

4)
numbers = [10, -5, 25, -18, 40, -9, 7, -30, 50, -1]

try:
    index = int(input("Enter index (0-9): "))

    if numbers[index] >= 0:
        print("Positive Number")
    else:
        print("Negative Number")

except IndexError:
    print("Error: Invalid index.")

except ValueError:
    print("Error: Please enter a valid integer index.")