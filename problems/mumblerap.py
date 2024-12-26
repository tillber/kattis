# https://open.kattis.com/problems/mumblerap

input()
l = ""
n = []

for c in list(input()):
    if c.isdigit():
        l += c
    elif not l == "":
        n.append(int(l))
        l = ""

if not l == "":  # required if line ends with int
    n.append(int(l))

print(max(n))
