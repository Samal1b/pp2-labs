def palindrome(word):
    #here is checking if the word is a palindrome
    word = word.lower()
    if word == word[::-1]:
        return True
    return False
print(palindrome("level"))
