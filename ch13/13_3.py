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

def top_words(hist, n):
    
    result = []

    for word, freq in hist.items():
        result.append((freq, word))

    result.sort(reverse = True)

    return result[0:n]
    
hist = histogram('pg15.txt')


print(top_words(hist, 20))
