def f(i):
    return i + 2


def g(i):
    return i > 5


def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    holder = []
    for item in L:
        #print(item)
        #print(g(f(item)))
        if g(f(item)) == False:
            holder.append(item)
    for item in holder:
        L.remove(item)

    def find_largest(L):
        if len(L) == 0:
            largest_element = -1
        else:
            largest_element = L[0]
            for item in L:
                if item > largest_element:
                    largest_element = item
        return largest_element

    return find_largest(L)


A = [-1, 5, 3, 6]
B = [-10, -6, -9]
L = [23, 5, 1, 1, 0]

print(applyF_filterG(L, f, g))
print(L)






