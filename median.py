"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        median = 0
        midIndex = int(len(numbers) / 2)
        numbers.sort()
        if len(numbers) % 2 == 0:
            median = (numbers[midIndex] + numbers[midIndex-1]) / 2
            print(median)
        else:
            median = numbers[midIndex]
            print(median)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

