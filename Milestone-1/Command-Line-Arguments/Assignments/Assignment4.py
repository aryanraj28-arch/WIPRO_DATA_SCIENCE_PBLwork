**Assignment4**
1)
import sys

def main():
    # sys.argv[0] is always the script name itself.
    # We need at least 2 additional arguments for the two numbers.
    if len(sys.argv) < 3:
        print("Error: Please provide exactly two numbers as command line arguments.")
        print("Usage: python sum_args.py <number1> <number2>")
        sys.exit(1)
        
    try:
        # Command line arguments are always passed as strings, so we convert them to floats
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        
        # Calculate the sum
        total_sum = num1 + num2
        
        # Display the result
        print(f"The sum of {num1} and {num2} is: {total_sum}")
        
    except ValueError:
        print("Error: Both arguments must be valid numbers (integers or decimals).")
        sys.exit(1)

if __name__ == "__main__":
    main()

2)
import sys

def main():
    # Check if at least one argument (the name) is provided
    if len(sys.argv) < 2:
        print("Error: Please provide a username.")
        print("Usage: python greeting.py <your_name>")
        sys.exit(1)
        
    # Retrieve the name (joining multiple words if the user provides full name without quotes)
    username = " ".join(sys.argv[1:])
    
    # Display the greeting
    print(f"Hello, {username}! Welcome to the Python module.")

if __name__ == "__main__":
    main()

3)
import sys

def main():
    # Check if any numeric arguments were passed
    if len(sys.argv) < 2:
        print("Error: Please provide at least one number.")
        print("Usage: python average_args.py <num1> <num2> <num3> ...")
        sys.exit(1)
        
    try:
        # Convert all arguments (excluding the script name) into floats
        numbers = [float(arg) for arg in sys.argv[1:]]
        
        # Calculate sum and average
        total_sum = sum(numbers)
        average = total_sum / len(numbers)
        
        # Display the summary results
        print(f"Total numbers parsed: {len(numbers)}")
        print(f"Sum: {total_sum}")
        print(f"Average: {average:.2f}")
        
    except ValueError:
        print("Error: All arguments provided must be valid numbers.")
        sys.exit(1)

if __name__ == "__main__":
    main()