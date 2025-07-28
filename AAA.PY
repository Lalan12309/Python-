import sys

def countPromotionalPeriods(orders):
    n = len(orders)
    stack = []
    visible = 0
    for h in orders:
        cnt = 1
        while stack and stack[-1][0] < h:
            visible += stack[-1][1]
            stack.pop()
        if stack and stack[-1][0] == h:
            eq = stack[-1][1]
            visible += eq
            stack.pop()
            if stack:
                visible += 1
            cnt = eq + 1
        else:
            if stack:
                visible += 1
        stack.append((h, cnt))
    return visible - (n - 1)

if __name__ == "__main__":
    data = sys.stdin
    n = int(data.readline())
    orders = [int(data.readline()) for _ in range(n)]
    print(countPromotionalPeriods(orders))
