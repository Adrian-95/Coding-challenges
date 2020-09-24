# Return the number (count) of vowels in the given string.
# The input string will only consist of lower case letters and/or spaces.

def get_count(input_str):
    num_vowels = 0
    for char in input_str:
        if char in "aeiouAEIOU":
            num_vowels = num_vowels+1
    return num_vowels
