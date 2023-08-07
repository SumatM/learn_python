# 2. **Bubble Sort**: Implement the bubble sort algorithm in Python.
#     - *Input*: [64, 34, 25, 12, 22, 11, 90]
#     - *Output*: "[11, 12, 22, 25, 34, 64, 90]"


arr = [64, 34, 25, 12, 22, 11, 9]


for i in range(len(arr)):
    flag= False;
    for j in range(i+1,len(arr)):
       if arr[i]>arr[j]:
         temp = arr[i];
         arr[i]=arr[j]
         arr[j] = temp;
         flag = True;
    if flag==False:
       break;
       

print(arr);