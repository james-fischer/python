

def get_words():

    fin = open("words.txt")

    Words = []
    for line in fin:
        word = line.strip()
        Words.append(word)

    return Words




def is_anagram(word1, word2):

    if len(word1) != len(word2):
        return False
    else:
        t1 = list(word1)
        t2 = list(word2)
        t1.sort()
        t2.sort()

        if t1 == t2:
            return True
        else:
            return False


def find_anagrams(wordList):
    
    d = {}
    for word in wordList:
        t = list(word)
        t.sort()
        u = tuple(t)
        
        temp = d.get(u, 0)
        if temp == 0:
            d[u] = [word]
        else:
            d[u].append(word)

    return d

def remove_singles(d):

    result = []
    for i in d.values():
        if len(i) > 1:
            result.append(i)

    return result
    


def sort_anagrams(anagramList):
    

    t = [(len(i), i) for i in anagramList]


    t.sort(reverse = True)

    sorted = [i for (length, i) in t]

    return sorted


def filter_length(d, n):
    
    result = {}
    for word, anagrams in d.items():
        if len(word) == n:
            result[word] = anagrams

    return result





#Main

wordList = get_words()

#wordList = ['deltas', 'salted', 'a', 'bcd', 'generating', 'greatening', 'lasted', 'x', 'slated']

#print(sort_anagrams(find_anagrams(wordList)))


d = find_anagrams(wordList)

t = remove_singles(d)


#print(sort_anagrams(t))

eight = filter_length(d, 8)

print(sort_anagrams(remove_singles(eight))[0])
