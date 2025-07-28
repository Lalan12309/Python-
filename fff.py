import bisect

def useMinimumTokens(warehouse, catalog):
    W = sorted(warehouse)
    S = sum(W)
    results = []
    for a, b in catalog:
        if a + b <= S:
            results.append(0)
            continue
        C = b - S
        best = 10**30
        def cost(i):
            w = W[i]
            aug = max(0, a - w)
            back = max(0, C + w)
            return aug + back
        i1 = bisect.bisect_left(W, a)
        for j in (i1 - 1, i1):
            if 0 <= j < len(W):
                best = min(best, cost(j))
        i2 = bisect.bisect_right(W, S - b)
        for j in (i2 - 1, i2):
            if 0 <= j < len(W):
                best = min(best, cost(j))
        best = min(best, cost(0), cost(len(W) - 1))
        results.append(best)
    return results

def main():
    n = int(input().strip())
    warehouse = list(map(int, input().split()))
    q = int(input().strip())
    catalog = [tuple(map(int, input().split())) for _ in range(q)]
    answers = useMinimumTokens(warehouse, catalog)
    for ans in answers:
        print(ans)

if __name__ == "__main__":
    main()
