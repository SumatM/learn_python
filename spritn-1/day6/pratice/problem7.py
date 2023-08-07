#Write a Python function named calculate_average that takes an array of numbers as a parameter and returns their average. Test it with a list of numbers.


def findAverage(arr):
    sum = 0;
    for ele in arr:
        sum+=ele;

    return sum/len(arr);

print(findAverage([1,2,3,4,5]))