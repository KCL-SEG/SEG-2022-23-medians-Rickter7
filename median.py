"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        median = 0
        middle = int(len(numbers) / 2)
        numbers.sort()
        if len(numbers) % 2 == 0:
            median = (numbers[middle] + numbers[middle-1]) / 2
            print(median)
        else:
            median = numbers[middle]
            print(median)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
