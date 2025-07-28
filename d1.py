from collections import defaultdict

def getConjugatePairs(s):
    cnt = defaultdict(int)
    cnt[(0, 0)] = 1
    da = dc = total = 0
    for ch in s:
        if ch == 'a':
            da += 1
        elif ch == 'b':
            da -= 1
        elif ch == 'c':
            dc += 1
        elif ch == 'd':
            dc -= 1
        total += cnt[(da, dc)]
        cnt[(da, dc)] += 1
    return total

if __name__ == "__main__":
    s = input().strip()
    print(getConjugatePairs(s))
