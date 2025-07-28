def findMinimumSum(power):
    total = 0
    for i in range(1, len(power)):
        if power[i] < power[i-1]:
            total += power[i-1] - power[i]
    return total

if __name__ == '__main__':
    n = int(input())
    power = list(map(int, input().split()))
    print(findMinimumSum(power))
