''' Write a Python program that removes all duplicates from a 
given list and prints the new list without duplicates. '''

arr = input("Enter a list of numbers: ")
input_user = list(map(int , arr.split()))
unique_elements = list(set(input_user))
print(unique_elements)

# Or

arr = input("Enter a list of numbers: ")
input_user = list(map(int, arr.split()))
unique_elements = []
for num in input_user:
    if num not in unique_elements:
        unique_elements.append(num)
        
print(unique_elements)

