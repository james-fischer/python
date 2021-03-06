def find(word, letter, index):
    #index = 0                                                                                         
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1



def count(s):
    count = 0
    for letter in s:
        if letter == 'a':
            count += 1
    return count



def count1(word, letter, index):
    count = 0
    
    index = find(word, letter, index)

    if index == -1:
        return 0
    else:
        while index > -1:
            count += 1
            index += 1
            index = find(word, letter, index)

        return count


print(count1("banana", "a", 0))
print(count1("banana", "x", 0))
print(count1("aaaaaa", "a", 0))
"""

first = find("banana", "a", 0)
print(first)
second = find("banana", "a", first+1)
print(second)
third = find("banana", "a", second+1)
print(third)
fourth = find("banana", "a", third+1)
print(fourth)
"""
