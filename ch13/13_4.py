import string

def histogram(filename):
    hist = {}
    fin = open(filename)
    for line in fin:
        process_line(line, hist)
    return hist


def process_line(line, hist):
    line = line.replace('-', ' ')


    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()


        hist[word] = hist.get(word, 0) +1

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

def top_words(hist, n=20):
    
    result = []

    for word, freq in hist.items():
        result.append((freq, word))

    result.sort(reverse = True)

    return result[0:n]



def get_words(file):
    
    fin = open(file)

    words = []
    for line in fin:
        word = line.strip()
        words.append(word)

    return words



def not_in_book(wordList, hist):
    results = []
    print(hist.keys())

    for word in wordList:
        if word not in hist.keys():
            results.append(word)

    return results


def subtract(d1, d2):
    results = {}
    for key in d1:
        if key not in d2:
            results[key] = None

    return results



wordList = get_words('words.txt')


hist = histogram('pg15.txt')

#print(hist)
print(not_in_book(wordList, hist))



"""    
hist = histogram('pg15.txt')


print(top_words(hist, 20))
"""
