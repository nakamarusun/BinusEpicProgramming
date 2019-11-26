#1
sampleData = "3, 5, 7, 23"
sampleData = sampleData.replace(",", "") # "3 5 7 23" string
newArr = sampleData.split() # [3,5,7,23] list
print(newArr)
print(tuple(newArr))

#2
def translateGaje(stnc: str):
    vowel = "aiueo "
    stnc = list(stnc)
    for i in stnc:
        if i not in vowel:
            stnc[stnc.index(i)] = i + 'o' + i
    return(''.join(stnc))

print(translateGaje("this is fun"))

#4
def isMember(char: str, list: [str]):
    for i in list:
        if char == i:
            return True
    return False

print(isMember("a", ["c", "b", "d"]))
print(isMember("d", ["c", "b", "d"]))

#5
def overlapping(list1: [str], list2: [str]):
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
def stringListToInt(list: [str]):
    intList: [int] = []
    for i in list:
        intList.append(len(i))
    return intList

print(stringListToInt(["aaaaa","bbbb"]))