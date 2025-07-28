def findMinimumOperations(items):
    total = sum(items)
    n = len(items)
    avg_low = total // n
    avg_high = avg_low + (1 if total % n != 0 else 0)
    excess = 0
    deficit = 0
    for item in items:
        if item > avg_high:
            excess += item - avg_high
        elif item < avg_low:
            deficit += avg_low - item
    return max(excess, deficit)

if __name__ == '__main__':
    n = int(input())
    items = []
    for _ in range(n):
        items.append(int(input()))
    result = findMinimumOperations(items)
    print(result)
