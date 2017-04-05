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


