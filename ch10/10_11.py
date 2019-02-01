from bisect import bisect_left

def in_bisect(t, value):
    
    i = bisect_left(t, value)
    if i != len(t) and t[i] == value:
        return True
    else:
        return False



def get_words():
    fin = open("words.txt")
    Words = []
    for line in fin:
        word = line.strip()
        Words.append(word)
    return Words


t = get_words()


for word in ['alien', 'allen', 'asdfasdf']:
    print(in_bisect(t, word))