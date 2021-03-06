def remove_duplicates(t):
    temp = t
    temp.sort()
    indices = []

    for i in range(len(temp)-1):
        
        if temp[i] == temp[i+1]:
            indices.append(i)

    i = len(temp)-1
    while i >= 0:
        if i in indices:
            temp.pop(i)
        i -= 1

    return temp



print(remove_duplicates([1,2,3,4]))
print(remove_duplicates([1,2,3,4,1,2,3]))
print(remove_duplicates([1,2,3,4,4]))
print(remove_duplicates(["a", "b", "c", "d", "d", "b"]))
