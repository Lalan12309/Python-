import string

def findLongestRegex(x, y, z):
    n = min(len(x), len(y))
    FULL = string.ascii_uppercase
    candidates = [i for i in range(n) if z[i] not in (x[i], y[i])]
    if not candidates:
        return "-1"
    block_at = max(candidates)
    parts = []
    for i in range(n):
        if i == block_at:
            allowed = [c for c in FULL if c != z[i]]
        else:
            allowed = list(FULL)
        parts.append("[" + "".join(allowed) + "]")
    return "".join(parts)

if __name__ == "__main__":
    x = input().strip()
    y = input().strip()
    z = input().strip()
    print(findLongestRegex(x, y, z))
 