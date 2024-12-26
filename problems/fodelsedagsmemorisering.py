# https://open.kattis.com/problems/fodelsedagsmemorisering

bday_map = {}
for _ in range(int(input())):
    s, c, d = input().split()
    (_, c2, _) = bday_map.get(d, (None, None, None))
    if c2 is None or c > c2:
        bday_map[d] = (s, c, d)

print(len(bday_map))
for f in list(bday_map.values()):
    print(f[0])
