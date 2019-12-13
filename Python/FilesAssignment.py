#1

# import string

# with open("Remarks by Bill Nye.txt", "r", encoding="utf-8") as file:
#     for lines, l in enumerate(file):
#         pass
#     hapax: {str: bool} = {}
#     for i in range(lines + 1):
#         curLine = file.readline()
#         lineArr = curLine.translate(str.maketrans(',./<>?;:"[]-=_+)(*&^$#@!', '                        ')).lower().split()
#         print(curLine)
#         input()
#         for lexicon in lineArr:
#             if lexicon not in hapax:
#                 hapax[i] = True
#             else:
#                 hapax[i] = False

#     file.close()
#     for i in hapax:
#         if i:
#             print(i)

#5

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