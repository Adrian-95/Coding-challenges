#Given an array of integers, find the one that appears an odd number of times.

#There will always be only one integer that appears an odd number of times.

def find_it(arr):
    res = 0
    for element in arr: 
        res = res ^ element 
    return res 
  