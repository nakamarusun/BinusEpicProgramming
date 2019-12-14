import time

pokemons = """ audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute
gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp
magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede
scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask """

pokemonsList = pokemons.lower().split()

longestChain = []

def findNextName(curName: str, curChain: [str]):
    global longestChain
    for nextName in pokemonsList:
        if curName[-1] == nextName[0] and nextName not in curChain:
            if len(curChain + [nextName]) > len(longestChain):
                longestChain = curChain + [nextName]
            findNextName(nextName, curChain + [nextName])

startTime = time.time()

for names in pokemonsList:
    findNextName(names, [names])

print(longestChain)
print(time.time() - startTime)