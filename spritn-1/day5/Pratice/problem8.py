# Create a dictionary representing a student with keys for name, age, and subjects (a list of subjects they are studying). Use a loop to print each subject.

student = {
  "name":"sumat",
  'age':21,
  'subject':['math','english','science','sanskrit']
}

for subject in student["subject"]:
    print(subject);


student["place"]='bbsr';

print(student);


for key in student.values():
   print(key)