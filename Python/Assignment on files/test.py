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
longestCount = 0

def findNextName(curChain: [str]):
    global longestChain
    global longestCount
    try:
        for wordAlph in pokemonDictionary[curChain[-1][-1]]:
            if wordAlph not in curChain:
                if len(curChain + [wordAlph]) > longestCount:
                    longestChain = curChain + [wordAlph]
                    longestCount = len(curChain + [wordAlph])
                findNextName(curChain + [wordAlph])
    except:
        pass

startTime = time.time()

for names in pokemonsList:
    findNextName([names])

print(longestChain)
print("Maximum result: ", len(longestChain))
print(time.time() - startTime)