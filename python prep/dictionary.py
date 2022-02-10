student = {'name':'Shubham','age': 24, 'courses': ['maths', 'CompSci']}

#Update/Add new item in dictionary
student['phone'] = '9717540209'

#best method to add update all in 1 one shot
student.update({'name': 'Shubham', 'batch': '2020-2022'})

#to find all the keys of dictionary
print(student.keys())
#To find all the values of dictionary
print(student.values())
#Print both key and values
print(student.items())
print(student)

#for loop iterations
for key in student:
    print(key)
for key, value in student.items():
    print(key, value) 


#use pop/delete method to delete key-value pair from Dictionary
del student['courses']
student.pop('age') 
name = student.pop('name')

#print(student.get('phone', 'Key value not found'))
print(student)
print(name)