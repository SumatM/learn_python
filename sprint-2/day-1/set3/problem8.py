# 1. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"



def readFile(path):

    with open(path,'r') as file:
        content = file.read();
        words = content.split();
        return (len(words));




print(readFile('./input.txt'))
















# # read 

# with open('problem5.py','r') as file:
#     content = file.read()
#    # print(content);


# with open('demo.txt','r') as file:
#     content = file.read();
    
# arr  = []

# arr.append(content);

# #print(arr);


# with open('demo.json','r') as file:
#     for line in file:
#         print(line.strip());

# # how to read json file and how to handle data out of it.

# #write;

# with open('demo.txt','a') as file:
#     file.write(' \n hello, This is written to the file.');


# with open('demo.txt','r') as file:
#     content = file.read();
#     print(content);


# with open('img.png','rb') as file:
#     content = file.read();
#     print(content);

# with open ('img.png',"wb") as file:
#     file.write('10 1001 1000111')