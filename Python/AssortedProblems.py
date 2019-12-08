import calendar

#1
sampleData = "3, 5, 7, 23"
sampleData = sampleData.replace(",", "") # "3 5 7 23" string
newArr = sampleData.split() # [3,5,7,23] list
print(newArr)
print(tuple(newArr))

#2
def translateGaje(stnc: str) -> str:
    vowel = "aiueo "
    stnc = list(stnc)
    for i in stnc:
        if i not in vowel:
            stnc[stnc.index(i)] = i + 'o' + i
    return(''.join(stnc))

print(translateGaje("this is fun"))

#3
def calendarMonth(m: int, y: int):
    print(calendar.month(y, m))

calendarMonth(11,2019)

#4
def isMember(char: str, list: [str]) -> bool:
    for i in list:
        if char == i:
            return True
    return False

print(isMember("a", ["c", "    alphabet = alphabet.split()b", "d"]))
print(isMember("d", ["c", "b", "d"]))

#5
def overlapping(list1: [str], list2: [str]) -> bool:
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

print(overlapping(["c", "a", "o"], ["c", "b", "d"]))
print(overlapping(["z", "a", "o"], ["c", "b", "d"]))

#6
def histogram(list: [int]):
    for i in list:
        print("*" * i)

histogram([5,3,6])

#7
def stringListToInt(list: [str]) -> [int]:
    intList: [int] = []
    for i in list:
        intList.append(len(i))
    return intList

print(stringListToInt(["aaaaa","bbbb"]))

#8
def findLongestWord(words: [str]) -> int:
    leng = 0
    for i in words:
        if leng < len(i):
            leng = len(i)
    return leng

print(findLongestWord(["amss","jotaro","dio"]))

#9
def filterLongWords(words: [str], n: int) -> [str]:
    newWords: [str] = []
    for i in words:
        if len(i) > n:
            newWords.append(i)
    return newWords

print(filterLongWords(["jojop", "kokopooo", "usingint"], 6))

#10
def pangram(stnc: str) -> bool:
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    for i in alphabet:
        if i not in stnc.lower():
            return False
    return True

print(pangram("The quick brown fox jumps over the lazy dog"))

#11
def charFreq(word: str) -> str:
    output: str = ""
    while word != "":
        output = output + word[0] + " x " + str(word.count(word[0])) + "\n"
        word = word.replace(word[0],"")
    return output

print(charFreq("anjayyyyy"))

#12
def encodeROT13(word: str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rot13 = alphabet[13:] + alphabet[:13]
    newStr = ""
    for i in word:
        newStr += rot13[alphabet.index(i)]
    return newStr

def decodeROT13(word: str) -> str:
    alphabet = "nopqrstuvwxyzabcdefghijklm"
    rot13 = alphabet[13:] + alphabet[:13]
    newStr = ""
    for i in word:
        newStr += rot13[alphabet.index(i)]
    return newStr

#13
def makeForms(verb: str) -> str:
    newVerb = ""
    suffixES = ["o", "ch", "s", "sh", "x", "z"]
    if verb.endswith("y"):
        newVerb += verb[:-1] + "ies"
        return newVerb
    for i in suffixES:
        if verb.endswith(i):
            newVerb += verb + "es"
            return newVerb
    return newVerb

print(makeForms("macho"))

#14
def addIng(verb: str) -> str:
    if verb.endswith("ie"):
        return verb[:-2] + "ying"
    if verb.endswith("e"):
        return verb[:-1] + "ing"
    vowel = "aiueo"
    if verb[-3] not in vowel and verb [-2] in vowel and verb[-1] not in vowel:
        return verb + verb[-1] + "ing"
    return verb + "ing"

print(addIng("maceh"))