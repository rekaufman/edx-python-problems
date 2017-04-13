def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    fList = []
    # print(fList)
    for item in aList:
        if type(item) == int or type(item) == str:
            fList.append(item)
            #       print("in if fList =", fList)
        elif type(item) == list:
            fList.extend(flatten(item))
            #      print("in elif fList =", fList)
    return fList


aList = [1, 'a', [2, "b"]]
print(flatten(aList))
