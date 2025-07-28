import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    N = int(input())
    m = int(input())
    Q = int(input())

    names = [input().strip() for _ in range(N)]
    idx = {name: i for i, name in enumerate(names)}

    parent = [-1] * N
    children = [[] for _ in range(N)]
    for i in range(1, N):
        p = (i - 1) // m
        parent[i] = p
        children[p].append(i)

    locked_by = [0] * N
    locked_desc_count = [0] * N

    def can_lock(u):
        v = parent[u]
        while v != -1:
            if locked_by[v]:
                return False
            v = parent[v]
        return locked_desc_count[u] == 0

    def update_ancestors(u, delta):
        v = parent[u]
        while v != -1:
            locked_desc_count[v] += delta
            v = parent[v]

    def lock(u, uid):
        if locked_by[u] or not can_lock(u):
            return False
        locked_by[u] = uid
        update_ancestors(u, 1)
        return True

    def unlock(u, uid):
        if locked_by[u] != uid:
            return False
        locked_by[u] = 0
        update_ancestors(u, -1)
        return True

    def upgrade(u, uid):
        if locked_by[u] or locked_desc_count[u] == 0:
            return False
        v = parent[u]
        while v != -1:
            if locked_by[v]:
                return False
            v = parent[v]

        stack = [u]
        to_unlock = []
        while stack:
            x = stack.pop()
            if locked_by[x]:
                to_unlock.append(x)
            for c in children[x]:
                if locked_desc_count[c] > 0 or locked_by[c]:
                    stack.append(c)

        for x in to_unlock:
            if locked_by[x] != uid:
                return False

        for x in to_unlock:
            locked_by[x] = 0
            update_ancestors(x, -1)

        locked_by[u] = uid
        update_ancestors(u, 1)
        return True

    out = []
    for _ in range(Q):
        t, name, uid = input().split()
        u = idx[name]
        uid = int(uid)
        if t == '1':
            res = lock(u, uid)
        elif t == '2':
            res = unlock(u, uid)
        else:
            res = upgrade(u, uid)
        out.append('true' if res else 'false')

    sys.stdout.write('\n'.join(out))

if __name__ == '__main__':
    main()
