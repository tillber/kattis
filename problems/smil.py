# https://open.kattis.com/problems/smil

row = input()
for smil in (":)", ";)", ":-)", ";-)"):
    start = 0
    while (i := row.find(smil, start)) > -1:
        print(i)
        start = i + 1
