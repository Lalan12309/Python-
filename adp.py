

def calculateMaxZeroes(sequenceData):
    count = 0
    current_min = float('inf')
    for x in sequenceData:
        if x <= current_min:
            count += 1
            current_min = x
    return count

if __name__ == "__main__":
    n = int(input())
    sequenceData = [int(input()) for _ in range(n)]
    print(calculateMaxZeroes(sequenceData))
