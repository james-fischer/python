def is_palindrome(word):
    if word == word[::-1]:
        print("Palindrome baby")
        return True
    else:
        print("Nope")
        return 


is_palindrome("ipalindromei")
