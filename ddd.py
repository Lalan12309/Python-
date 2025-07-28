from collections import Counter

def calculateMinimumDeliveries(packageSizes):
    trips = 0
    for v in Counter(packageSizes).values():
        if v == 1:
            return -1
        if v % 3 == 0:
            trips += v // 3
        elif v % 3 == 1:
            if v < 4:
                return -1
            trips += (v - 4) // 3 + 2
        else:
            trips += v // 3 + 1
    return trips

def main():
    n = int(input())
    packageSizes = list(map(int, input().split()))
    print(calculateMinimumDeliveries(packageSizes))

if __name__ == "__main__":
    main()
