#Create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

def filter_list(l):
    filtered_list = [char for char in l if type(char) == int]
    return filtered_list