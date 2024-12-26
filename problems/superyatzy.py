# https://open.kattis.com/problems/superyatzy

d = []
cnt = {}

n, m = map(int, input().split())

for i in range(n):
    d.append(x := int(input()))
    cnt[x] = cnt.get(x, 0) + 1

cnt_n = 0
c = max(cnt, key=cnt.get)

for i in d:
    if i == c:
        continue
    cnt_n += 1
    if cnt_n > m:
        print("Nej")
        exit()

print("Ja")
