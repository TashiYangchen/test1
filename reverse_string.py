def reverse_string(s):
    # Base case: if the string is empty or has only one character, return it
    if len(s) <= 1:
        return s
    # Recursive case: reverse the substring starting from the second character
    # and concatenate the first character at the end
    else:
        return reverse_string(s[1:]) + s[0]

# Test cases
print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("python")) # Output: "nohtyp"
print(reverse_string(""))        # Output: ""