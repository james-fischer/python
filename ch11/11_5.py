def invert_dict(d):
    
    inverse = {}
    for key, val in d.iteritems():
        inverse.setdefault(val, []).append(key)
    return inverse


d = dict(a=1, b=2, c=3, z = 1)

inverse = invert_dict(d)
for val, keys in inverse.iteritems():
    print val, keys
