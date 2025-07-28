def getMaximumPairs(frontend, backend):
    frontend.sort()
    backend.sort()
    i = j = 0
    count = 0
    n = len(frontend)
    while i < n and j < n:
        if frontend[i] > backend[j]:
            count += 1
            i += 1
            j += 1
        else:
            i += 1
    return count

if __name__ == "__main__":
    # read s and its s lines
    s = int(input().strip())
    frontend = [int(input().strip()) for _ in range(s)]
    # read s2 and its s2 lines
    s2 = int(input().strip())
    backend  = [int(input().strip()) for _ in range(s2)]
    # compute and print
    print(getMaximumPairs(frontend, backend))