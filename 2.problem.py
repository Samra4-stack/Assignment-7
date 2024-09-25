''' Given a list of fruits: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango'],
write a program to:
Access the first, middle, and last element of the list.
Change the second element to 'blueberry'.  '''

arr = ['Apple', 'Banana', 'Cherry', 'Orange', 'Kiwi', 'Mango']
print(f"Your list contains {arr}")
arr[1] = 'Strawberry'
print(f"Updated list: {arr}")
print(f"Your first element in list:  {arr[0]}")
print(f"Your middle element in list:  {arr[2]}")
print(f"Your Last element in list:  {arr[-1]}")

# OR

arr1 = input("Enter a list of 5 numbers: ")
user_input = list( arr1.split())
number = 0 
while number < 1:
    print (user_input)
    ask  = input('Add new element in list: ')
    no = int(input("At what number you want to add: "))
    user_input[no] = ask
    print(f"Updated list: {user_input}")
    first_element = user_input[0]
    print(f"First element of list is: {first_element}")
    last_element = user_input[-1]
    print(f"Last element of list is: {last_element}")
    length = len(user_input)
    if length%2 == 1:
        middle_element = user_input[length//2]
        print(f"Middle element of list is: {middle_element}")
    else:
        middle_element1 = user_input[length//2 - 1]
        middle_element2 = user_input[length//2]
        print(f"Middle elements of list are: {middle_element1} and {middle_element2}")
    number += 1
    
