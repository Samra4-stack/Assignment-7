''' Write a program to update the 'grade' value to 'A', and 
add a new key-value pair for 'major' with the value 'Computer Science'.
student = {'name': 'John', 'age': 22, 'grade': 'B'} '''

bio_data = {
    'name': 'John', 
    'age': 22, 
    'grade': 'B'
}
bio_data.update({'grade': 'A'})
bio_data['grade'] = 'A'
bio_data['major'] = 'Computer Science'
print(bio_data)