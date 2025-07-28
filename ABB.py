#!/usr/bin/python3
import os
import sys
import string

def findLongestRegex(x, y, z):
    n = min(len(x), len(y))
    FULL = list(string.ascii_uppercase)
    candidates = [i for i in range(n) if z[i] not in (x[i], y[i])]
    if not candidates:
        return "-1"
    block_at = max(candidates)
    parts = []
    for i in range(n):
        if i == block_at:
            allowed = set(FULL)
            allowed.remove(z[i])
            chars = sorted(allowed)
        else:
            chars = FULL
        parts.append("[" + "".join(chars) + "]")
    return "".join(parts)

if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    x = sys.stdin.readline().strip()
    y = sys.stdin.readline().strip()
    z = sys.stdin.readline().strip()
    fptr.write(findLongestRegex(x, y, z) + "\n")
    fptr.close()
