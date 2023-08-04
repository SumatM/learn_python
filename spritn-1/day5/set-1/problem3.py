# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."



students = [2,1,3,8,7,10,4,6,5,9]

students.append(20)

print(students)

students.pop()

print(students);

students.sort()

print(len(students));

print(students);

students.sort(reverse=True)

print(students);

