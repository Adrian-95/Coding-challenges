#An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    initial_string = string.lower()
    letter_list =[]
    for letter in initial_string: 
            if letter.isalpha(): 
                if letter in letter_list: 
                    return False
            letter_list.append(letter) 
    return True