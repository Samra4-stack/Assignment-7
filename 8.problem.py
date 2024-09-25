''' Write a program that creates a dictionary where the keys are subjects 
(e.g., 'Math', 'Science') and the values are lists of marks. Add marks for 3 subjects, and
print the average marks for each subject'''

def average():
    marks = {
        'Math': [78,54,34],
        'Science': [85,54,85],
        'English': [80,32,90]
    }

    for subject,scores in marks.items():
      avg= sum(scores) / len(scores)
      print(f'Average marks for {subject}: {avg}')
    
average()