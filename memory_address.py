def find_first_repeating_character(s):
    # Dictionary to store count of characters
    char_count = {}
    
    # Iterate through each character in the string
    for char in s:
        if char in char_count:
            # If character is already in the dictionary, it is repeating
            address = id(char)
            print(f"The memory address of the first repeating character '{char}' is: {address}")
            return char
        else:
            # Add character to dictionary with count 1
            char_count[char] = 1
            
    # If no repeating character is found
    return None

# Example usage with a string where 'p' is the first repeating character
example_string = "happy_programming"
result = find_first_repeating_character(example_string)
if result:
    print("First repeating character:", result)
else:
    print("No repeating character found.")


