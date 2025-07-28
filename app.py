import sys

def findMaxRegexMatch(sourceString, pattern):
    idx = pattern.find('*')
    prefix = pattern[:idx]
    suffix = pattern[idx+1:]

    n = len(sourceString)
    if prefix:
        i = sourceString.find(prefix)
        if i == -1:
            return -1
    else:
        i = 0

    if suffix:
        j = sourceString.rfind(suffix)
        if j == -1:
            return -1
    else:
        j = n

    if j < i + len(prefix):
        return -1

    return j + len(suffix) - i

if __name__ == "__main__":
    s = input().strip()
    p = input().strip()
    print(findMaxRegexMatch(s, p))
    
