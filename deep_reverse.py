def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    def reverse_Sublist(sublist):
        reversed_sublist = []
        for i, _ in enumerate(sublist):
            reversed_sublist.append(sublist[(i + 1) * -1])
        return reversed_sublist

    for counter, item in enumerate(L):
        L[counter] = reverse_Sublist(item)

    lenL = len(L)
    L.extend(L)
    last = -1
    first = 0
    for a in range(lenL):
        # print("At beginning, last is now {}".format(last))
        # print("L is {}".format(L))
        # print("Setting the {}th element of L ({}) to the {}th element of L ({})".format(
            # last, L[last], first, L[first]))
        L[last] = L[first]
        # print("L is now {}".format(L))
        # print("Before decrementing, last is now {}".format(last))
        last -= 1
        # print("After decrementing, last is now {}".format(last))
        first += 1
    x = 0
    while x < lenL:
        # print("L before deletion: {}".format(L))
        L.pop(0)
        # print("L after deletion: {}".format(L))
        x += 1


    #print("the newlist is ", newList)

tavi = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(tavi)
print("New tavi: {}".format(tavi))