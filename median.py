"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from re import A
from unittest import result


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

# sort the numbers in ascending order
numbers.sort()

# find the list length and then the median
listLength = len(numbers)
result = None

if listLength %2 == 0 :
    lowerNum = numbers[int((listLength / 2) - 1)]
    higherNum = numbers[int(listLength / 2)]
    result = (lowerNum + higherNum) / 2
else:
    result = numbers[int((listLength - 1) / 2)]

print(result);