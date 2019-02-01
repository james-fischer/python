def first(word):
    return  word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]



#print(first("Seahawks"))
#print(last("Seahawks"))
#print(middle("Seahawks"))

#print(middle("ab"))
#print(middle("a"))
#print(middle(""))



def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        print("Palindrome!")
    elif first(word) == last(word):
        is_palindrome(middle(word))
    else:
        print("Try again, dummy!")

    return None


is_palindrome("")
is_palindrome("a")
is_palindrome("ab")
is_palindrome("yobananaboy")
is_palindrome("abc")
is_palindrome("amanaplanacanalpanama")
