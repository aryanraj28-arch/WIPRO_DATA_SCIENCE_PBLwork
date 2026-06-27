**Mini_project2**

# 1. Create a dictionary with people and an interesting fact about each
people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# 2. Display each person and their interesting fact
print("--- Initial List ---")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

print()  # Blank line for readability

# 3. Change a fact about one of the people
people_facts["Jeff"] = "Is afraid of heights."

# 4. Add an additional person and corresponding fact
people_facts["Jill"] = "Can hula dance."

# 5. Display the new list of people and facts
print("--- Updated List ---")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

2)
def find_runner_up(scores):
    # 1. Remove duplicates by converting the list to a set
    unique_scores = set(scores)
    
    # 2. Remove the maximum score from the set
    unique_scores.remove(max(unique_scores))
    
    # 3. The new maximum is the runner-up score
    runner_up = max(unique_scores)
    
    return runner_up

# --- Testing the code with your sample input ---
sample_input = [2, 3, 6, 6, 5]
output = find_runner_up(sample_input)

print(f"Runner-up score: {output}")

3)
# Step 1: Read the number of students
n = int(input("Enter number of students: "))

# Step 2: Initialize an empty dictionary to store records
student_marks = {}

# Step 3: Populate the dictionary with user input
for _ in range(n):
    # Split the input into name and marks
    line = input("Enter name and marks (Math Physics Chemistry): ").split()
    name = line[0]
    scores = list(map(float, line[1:]))
    student_marks[name] = scores

# Step 4: Get the query name
query_name = input("Enter a name to find average: ")

# Step 5: Calculate and print the average
if query_name in student_marks:
    marks = student_marks[query_name]
    average_marks = sum(marks) / len(marks)
    # Prints the average formatted to 2 decimal places
    print(f"Average percentage mark: {average_marks:.2f}")
else:
    print("Student record not found.")

4)
def count_alex_appearances():
    # Read the input string from the user
    input_string = input()
    
    # Count the occurrences of the substring "Alex"
    alex_count = input_string.count("Alex")
    
    # Print the final count
    print(alex_count)

# Execute the function
if __name__ == "__main__":
    count_alex_appearances()