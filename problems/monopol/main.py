from decimal import Decimal


def probability(distances: tuple) -> Decimal:
    cnt = 0
    for dist in distances:
        for i in range(1, 7):
            for j in range(1, 7):
                if (i + j) == int(dist):
                    cnt += 1
    return cnt/36


def run():
    input()  # Input unused amount of opponents hotels
    hotels_dist = tuple(input().split())  # Input distances to opponents hotels
    print(probability(hotels_dist))


if __name__ == "__main__":
    run()
