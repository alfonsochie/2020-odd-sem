def removekeys(dict,list):
    for i in list:
        if i in dict:
            del dict[i]
    return dict

if __name__ =="__main__":
    key = input("enter key").split(",")
    value = input("enter value").split(",")
    dict = {}
    for i in range (len(key)):
        dict[key[i]] = value[i]
    list = input ("enter key to remove").spit(",")
    print(removekeys(dict,list))