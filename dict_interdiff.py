def f(a,b):
    return a + b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # loop through keys in d1 and see if they are in d2
    # if they are in d2, call f() of that key
    dict_inter = {}
    for key_i, value in d1.items():
        if key_i in d2:
            dict_inter[key_i] = f(d1[key_i], d2[key_i])

    # for difference, loop through d1, if not in d2,
    dict_diff = {}
    for pair in d1.items():
        key_d = pair[0]
        value_d = pair[1]
        if key_d not in d2:
            dict_diff[key_d] = value_d
    for pair in d2.items():
        key_di = pair[0]
        value_di = pair[1]
        if key_di not in d1:
            dict_diff[key_di] = value_di

    return (dict_inter, dict_diff)

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
a = dict_interdiff(d1, d2)
print(a)