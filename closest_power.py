def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # what are the exceptions
    if num == 1:
        exponent = 0
    for exponent in range(int(num)):
        if not abs(num - base**exponent) < abs(num - base**(exponent - 1)):
            exponent -= 1
            return exponent
    return exponent



def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    length = len(listA)
    pairwiseSum = 0
    for counter in range(length):
        pairwiseSum += listA[counter] * listB[counter]
    return pairwiseSum


def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    counter = 0
    pairwiseSum = 0
    while counter < len(listA):
        pairwiseSum += listA[counter] * listB[counter]
        counter += 1
    return pairwiseSum


def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    lenL = len(L)
    L.extend(L)
    last = -1
    first = 0
    for a in range(lenL):
        print("At beginning, last is now {}".format(last))
        print("L is {}".format(L))
        print("Setting the {}th element of L ({}) to the {}th element of L ({})".format(
            last, L[last], first, L[first])
        )
        L[last] = L[first]
        print("L is now {}".format(L))
        print("Before decrementing, last is now {}".format(last))
        last -= 1
        print("After decrementing, last is now {}".format(last))
        first += 1
    x = 0
    while x < lenL:
        print("L before deletion: {}".format(L))
        L.pop(0)
        print("L after deletion: {}".format(L))
        x += 1

    def reverse_Sublist(sublist):
        reversed_sublist = []
        for i, _ in enumerate(sublist):
            reversed_sublist.append(sublist[(i + 1) * -1])
        return reversed_sublist


    for item in L:
        reverse_Sublist(item)




    #print("the newlist is ", newList)

x = 1
y = 2
a = x
x = y
y = a

tavi = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(tavi)
print("New tavi: {}".format(tavi))