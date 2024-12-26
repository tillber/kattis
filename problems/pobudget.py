# https://open.kattis.com/problems/pobudget

cnt = int(input())
total = sum((input(), int(input()))[1] for _ in range(cnt))

if total > 0:
    print("Usch, vinst")
elif total < 0:
    print("Nekad")
else:
    print("Lagom")
