# 1. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"

arr =  [64, 25, 12, 22, 11]



for i in range(len(arr)):
    min = i;
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min]:
            min = j;
    print(arr[min],arr[i])
    temp = arr[i];
    arr[i]=arr[min];
    arr[min] = temp;
    
print(arr);
    