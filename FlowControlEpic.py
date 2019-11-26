#1
def max2(x, y):
    if x > y:
        return(x)
    else:
        return(y)

#2
def max3(x, y, z):
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    else:
        return z

#3
def length(arr):
    counter: int = 0
    for i in arr:
        counter = counter + 1
    return counter

#4
def checkVowel(vow: str):
    vowels: (str) = ("a", "i", "u", "e", "o")
    for i in vowels:
        if i == vow.lower:
            return True
    return False

#5
def reverse(word: str):
    return word[::-1]

#6
def isPalindrome(word: str):
    if word == word[::-1]:
        return True
    else:
        return False

#7
def isSentencePalindrome(stnc: str):
    