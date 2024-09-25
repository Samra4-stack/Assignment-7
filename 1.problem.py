'''  Write a Python program to create a list of 5 numbers. 
   Add an element to the list, remove one element, and find 
   the maximum and minimum number in the list. '''
   
arr = input("Enter a list of 5 numbers: ")
user_input = list(map(int , arr.split()))
number = 0
while number < 1:
    print (user_input)
    ask = int(input("Add an element to the list: "))
    user_input.append(ask)
    print(f"updated_list = {user_input}")
    remove = int(input("Remove an element from the list: "))
    user_input.remove(remove)
    print(f"updated_list = {user_input}")
    maximum = max(user_input)
    print(f"Maximum number in list = {maximum}") 
    minimum = min(user_input)
    print(f"Minimum number in list = {minimum}") 
    number += 1 