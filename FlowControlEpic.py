import string

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
    newStr = stnc.replace(" ", "")
    newStr = newStr.translate(str.maketrans("","", string.punctuation))
    newStr = newStr.lower()
    if newStr == newStr[::-1]:
        return True
    return False

#8
def generateNChars(n: int, c: str):
    return n*c

#9
def evaluateGrade(n: float):
    if n > 1 or n < 0:
        return "Error"
    if n < 0.6:
        return "F"
    if n < 0.7:
        return "D"
    if n < 0.8:
        return "C"
    if n < 0.9:
        return "B"
    return "A"

#10
def calculateGrossPay():
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))

    if hours > 40:
        print((rate*40 + (hours-40)*rate*1.5))
    else:
        print(rate*hours)

#11
def distanceFromZero(n):
    try:
        if n < 0:
            return n * -1
        return n
    except:
        return "Nope"

#12
def pigLatin(word: str):
    newStr = ""
    for i in range(1,len(word)):
        newStr = newStr + word[i]
    newStr = newStr + word[0] + "ay"
    return newStr.lower()

print(pigLatin("Python"))