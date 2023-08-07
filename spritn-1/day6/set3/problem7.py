# 1. **FizzBuzz**: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
#     - *Input*: None
#     - *Output*: "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16,..."




def printFizzBuzz(num):

    store = ""

    for i in range(1,num+1):
        if  i%5==0 and i%3==0:
            store+=" FizzBuzz "; 
        elif i%5==0:
           store+=" Buzz ";
        elif i%3==0:
          store+=" Fizz " 
        else:
            store+= f" {(i)} "

    return store;


print(printFizzBuzz(15))