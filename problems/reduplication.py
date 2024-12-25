import sys

word = ""
times = 0

for i, line in enumerate(sys.stdin):
    if i == 0:
        # Collect first line as the word (to reduplicate)
        word = line.strip()
        continue
    # Collect the second line as the amount of times to reduplicate the given word.
    times = int(line)
    break

print(word*times)
