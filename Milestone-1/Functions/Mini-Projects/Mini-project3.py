**Mini-project3**
1)
def sort_colors(color_sequence):
    # Split the hyphen-separated string into a list
    color_list = color_sequence.split('-')
    
    # Sort the list alphabetically
    sorted_list = sorted(color_list)
    
    # Join the sorted list back into a hyphen-separated string
    return '-'.join(sorted_list)

# --- Test Cases ---

# Sample Input 1
input1 = "green-red-yellow-black-white"
print(f"Input:  {input1}")
print(f"Output: {sort_colors(input1)}\n")

# Sample Input 2
input2 = "PINK-BLUE-TAN-PURPLE"
print(f"Input:  {input2}")
print(f"Output: {sort_colors(input2)}")

2)
def is_palindrome(name):
    """
    Checks whether the input name is a palindrome or not.
    Ignores spaces to handle multi-word inputs correctly.
    """
    # Remove spaces and convert to a uniform case (though input is specified as uniform)
    clean_name = name.replace(" ", "")
    if clean_name == clean_name[::-1]:
        return "Yes it is a palindrome."
    else:
        return "No it is not a palindrome."

def count_the_vowels(name):
    """
    Counts the number of vowels (a, e, i, o, u) present in the name.
    """
    vowels = "aeiouAEIOU"
    count = sum(1 for char in name if char in vowels)
    return f"No of vowels: {count}"

def frequency_of_letters(name):
    """
    Calculates how many times each letter appears in the name.
    Excludes spaces from the frequency breakdown.
    """
    freq_dict = {}
    for char in name:
        if char == " ":  # Skip spaces as per standard string analysis requirements
            continue
        freq_dict[char] = freq_dict.get(char, 0) + 1
        
    # Format the dictionary output into the required string format
    freq_pairs = [f"{key} - {value}" for key, value in freq_dict.items()]
    return "Frequency of letters: " + ", ".join(freq_pairs)
import string_utils

def run_test(sample_input):
    print(f"Input: {sample_input}")
    print(string_utils.is_palindrome(sample_input))
    print(string_utils.count_the_vowels(sample_input))
    print(string_utils.frequency_of_letters(sample_input))
    print("-" * 40)

if __name__ == "__main__":
    # Test Case 1
    run_test("bob")
    
    # Test Case 2
    run_test("marcel bentok tanaka")