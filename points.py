def calculateMaximumPointsEarned(pointValues):
    pointValues.sort(reverse=True)
    total = 0
    for i, v in enumerate(pointValues):
        if v <= i:
            break
        total += v - i
    return total

if __name__ == "__main__":
    n = int(input())
    values = [int(input()) for _ in range(n)]
    print(calculateMaximumPointsEarned(values))
