# # 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."


def checkPalindrom(str):
    bag="";
    i = len(str)-1
    while i>=0:
        bag+=str[i]
        i-=1
    print(bag);
    if(str==bag):
        return ("The word "+str+" is a palindrome")
    else:
        return ("The word "+str+" is a not a palindrome")



print(checkPalindrom('madam'))




# for and while loop pratice


for i in range(1,10,+2):
    print(i);


i = 1;

while i<=5:
    print(i);
    i+=1;