#Given two dictionaries, dict1 and dict2, find and print the common keys between them using a loop.

student = {
  "name": "sumat",
  'age': 21,
  'subject': ['math', 'english', 'science', 'sanskrit'],
  'place':'bbsr'
}

aman = {
  'name': 'aman',
  'age': 18,
  'subject': ['math', 'english', 'science', 'sanskrit']
}



for key in student.keys():
    if key in aman:
      print(key);