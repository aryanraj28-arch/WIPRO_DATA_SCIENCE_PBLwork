**Mini-project5**
1)import collections
import string

def solve_secret_message(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return

    # 1. Calculate the meeting time based on the number of lines
    num_lines = len(lines)
    
    # Handle edge case where file might be empty
    if num_lines == 0:
        print("The file is empty.")
        return

    if num_lines <= 12:
        meeting_time = f"{num_lines} AM"
    else:
        # Convert 24-hour style count to 12-hour PM format
        pm_time = num_lines - 12
        meeting_time = f"{pm_time} PM"

    # 2. Find the most frequent word for the meeting place
    all_words = []
    for line in lines:
        # Remove punctuation and split into words
        cleaned_line = line.translate(str.maketrans('', '', string.punctuation))
        words = cleaned_line.split()
        all_words.extend(words)

    if not all_words:
        print("No words found in the file.")
        return

    # Count frequencies of each word
    word_counts = collections.Counter(all_words)
    
    # Get the most common word
    most_common_word, _ = word_counts.most_common(1)[0]
    meeting_place = f"{most_common_word} Street"

    # Print the final output format matches the sample
    print(f"Meeting time: {meeting_time}")
    print(f"Meeting place: {meeting_place}")

# To run the script, pass the path of your text file:
# solve_secret_message("Sample.txt")