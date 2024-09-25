''' Write a program that takes a list of integers and prints:
The first 3 elements
The last 2 elements
The entire list in reverse order '''

arr = input("Enter a list of 5 numbers: ")
user_input = list(map(int , arr.split()))
print(f"First 3 elements of list: {user_input[0:3]}")
print(f"Last 2 elements of list: {user_input[-2:]}")
print(f"The entire list in reverse order: {list(reversed(user_input))}")