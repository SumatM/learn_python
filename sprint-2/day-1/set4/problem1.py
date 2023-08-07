# 1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
#     - *Input*: "cinema", "iceman"
#     - *Output*: "True"



def checkAnagram(str):
    bag = "";
    dictionary={}
    for char in str:
        dictionary[char] = 1 or dictionary[char]

    print(dictionary);


checkAnagram('cinemac');