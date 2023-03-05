# get a number from the user to find if it can be made by adding consecutive numbers incremented by an inputed variable
from typing import List

# prompt user for a target number and a incrementer
target = int(input("Enter a target number: "))
incrementer = int(input("Enter a incrementer: "))
# if intrementer is 0 or less, set it to 1
if incrementer <= 0:
    incrementer = 1

# create method to calculate sum of consecutive numbers from 1 to n
def sum_of_consecutive_numbers(n):
    return (n * (n + 1)) / 2

# create method to find if a number can be made by adding consecutive numbers incremented by an inputed variable
def find_consecutive_sequence(target, incrementer) -> List[int]:
    # create a list to hold the numbers
    numbers = []
    # create a variable to hold the sum of the numbers
    sum = 0
    # create a variable to hold the number of consecutive numbers
    n = 1
    # loop until the sum of the numbers is greater than the target
    while sum < target:
        # add the sum of the consecutive numbers to the sum
        sum += sum_of_consecutive_numbers(n)
        # if the sum is less than the target
        if sum < target:
            # add the sum to the list of numbers
            numbers.append(sum)
        # increment the number of consecutive numbers
        n += 1
    # if the sum is equal to the target
    if sum == target:
        # add the sum to the list of numbers
        numbers.append(sum)
    # return the list of numbers
    return numbers


# call the method to find if a number can be made by adding consecutive numbers incremented by an inputed variable
numbers = find_consecutive_sequence(target, incrementer)
# if the list of numbers is empty
if not numbers:
    # print that the number cannot be made
    print("The number cannot be made by adding consecutive numbers incremented by", incrementer)
# if the list of numbers is not empty
else:
    # print the list of numbers
    print("The number can be made by adding consecutive numbers incremented by", incrementer, ":", numbers)