# https://open.kattis.com/problems/monopol

hotels_cnt = input()
hotels_dist = tuple(input().split())

cnt = 0
for dist in hotels_dist:
    for i in range(1, 7):
        for j in range(1, 7):
            if (i + j) == int(dist):
                cnt += 1

print(cnt/36)
