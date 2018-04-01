
from collections import Counter

def mix(s1, s2):
    c1 = Counter(filter(str.islower, s1))
    c2 = Counter(filter(str.islower, s2))
    res = []
    # for c in set(c1.keys() + c2.keys()):
    print(set(list(c1)+list(c2)))
    for c in set(list(c1) + list(c2)):
        n1, n2 = c1.get(c, 0), c2.get(c, 0)
        if n1 > 1 or n2 > 1:
            res.append(('1', c, n1) if n1 > n2 else
                ('2', c, n2) if n2 > n1 else ('=', c, n1))
        print(res)
    res = ['{}:{}'.format(i, c * n) for i, c, n in res]
    print(res)
    return '/'.join(sorted(res, key=lambda s: (-len(s), s)))

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
print(mix(s1, s2))
