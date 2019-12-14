#1 #####################################################
with open("Remarks by Bill Nye.txt", "r", encoding="utf-8") as file:
    curLine = file.readlines()
    file.close()

hapax: {str: bool} = {}
for lines in curLine:
    lineArr = lines.translate(str.maketrans(',./<>?;:"[]-=_+)(*&^$#@!”', '                         ')).translate(str.maketrans('1234567890', '          ')).lower().split()
    for words in lineArr:
        if words not in hapax:
            hapax[words] = True
        else:
            hapax[words] = False

for words in hapax:
    if hapax[words]:
        print(words)

#2 #####################################################
fileName = "test.txt"
with open(fileName, "r", encoding="utf-8") as file:
    lineList = file.readlines()
    file.close()

with open(("Numbered" + fileName), "w+", encoding="utf-8") as file:
    for i in range(len(lineList)):
        file.write("{}. {}".format(str(i + 1), lineList[i]))
    file.close()

#3 #####################################################
with open("Remarks by Bill Nye.txt", "r", encoding="utf-8") as file:
    curLine = file.readlines()
    file.close()

count: int = 0
sumWords: int = 0
for lines in curLine:
    lineArr = lines.translate(str.maketrans(',./<>?;:"[]-=_+)(*&^$#@!”', '                         ')).translate(str.maketrans('1234567890', '          ')).lower().split()
    for words in lineArr:
        count += 1
        sumWords += len(words)

print(sumWords/count)

#4 #####################################################
import time

pokemons = """ audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute
gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp
magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede
scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask """

pokemonsList = pokemons.lower().split()
pokemonDictionary = {}
for names in pokemonsList:
    if names[0] not in pokemonDictionary:
        pokemonDictionary[names[0]] = []
    pokemonDictionary[names[0]].append(names)

longestChain = []

def findNextName(curChain: [str]):
    global longestChain
    try:
        for wordAlph in pokemonDictionary[curChain[-1][-1]]:
            if wordAlph not in curChain:
                if len(curChain + [wordAlph]) > len(longestChain):
                    longestChain = curChain + [wordAlph]
                findNextName(curChain + [wordAlph])
    except:
        pass

startTime = time.time()

for names in pokemonsList:
    findNextName([names])

print(longestChain)
print("Maximum result: ", len(longestChain))
print(time.time() - startTime)

#5 #####################################################
def sentenceSplitter(longString: str) -> str:
    titles: (str) = ("mr", "mrs", "dr", "ms", "sr", "jr", "i.e")
    wordsList: [str] = longString.split()

    for word in range(len(wordsList)):
        checkPeriod = wordsList[word][-1] == "."
        checkNotTitle = wordsList[word][:-1].lower() not in titles
        checkExclmQstn = wordsList[word][-1] == "?" or wordsList[word][-1] == "!"

        if ((checkPeriod and checkNotTitle) or checkExclmQstn):
            wordsList[word] = wordsList[word] + "\n"
    return " ".join(wordsList)

mySentence = "Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."

print(sentenceSplitter(mySentence))