import bisect
def minimizeMaxParcelLoad(initialParcels, additionalParcels):
    initialParcels.sort()
    n = len(initialParcels)
    prefix = [0] * (n+1)
    for i, v in enumerate(initialParcels):
        prefix[i+1] = prefix[i] + v

    lo = initialParcels[-1]
    hi = lo + additionalParcels

    while lo < hi:
        mid = (lo + hi) // 2
        i = bisect.bisect_left(initialParcels, mid)
        cap = mid * i - prefix[i]
        if cap >= additionalParcels:
            hi = mid
        else:
            lo = mid + 1
    return lo

def main():
    n = int(input().strip())                  # reads “5”
    initial = list(map(int, input().split())) # reads “7 5 9 1 3”
    extra = int(input().strip())              # reads “25”
    print(minimizeMaxParcelLoad(initial, extra))
 
if __name__ == "__main__":
    main()
