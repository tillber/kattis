import sys
from decimal import Decimal


def probability(distances: tuple) -> Decimal:
    cnt = 0
    for dist in distances:
        for i in range(1, 7):
            for j in range(1, 7):
                if (i + j) == dist:
                    cnt += 1
    return cnt/36


def run():
    hotels_cnt = None
    hotels_dist = ()

    for i, line in enumerate(sys.stdin):
        if i == 0:
            # Collect first line as the amount of the opponents hotels
            hotels_cnt = int(line)
            continue
        # Collect the second line as the distances to each of the oppopents hotels
        hotels_dist = tuple(int(d) for d in str.split(line.strip(), " "))
        break

    print(probability(hotels_dist))


if __name__ == "__main__":
    run()
