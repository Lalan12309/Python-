def optimize_tree_height(N, K, parent_list):
    from collections import deque, defaultdict

    graph = defaultdict(list)
    children = set()
    for child, parent in enumerate(parent_list, start=1):
        graph[parent].append(child)
        children.add(child)

    # Find the root (node that is not anyone's child)
    root = next(node for node in range(1, N + 1) if node not in children)

    def bfs(root, removed):
        queue = deque([(root, 0)])
        visited = set(removed)
        max_depth = 0
        while queue:
            node, depth = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            max_depth = max(max_depth, depth)
            for neighbor in graph[node]:
                queue.append((neighbor, depth + 1))
        return max_depth

    # Try removing up to K deepest subtrees
    def find_deepest_nodes(root):
        queue = deque([(root, 0)])
        depths = []
        while queue:
            node, depth = queue.popleft()
            depths.append((depth, node))
            for neighbor in graph[node]:
                queue.append((neighbor, depth + 1))
        depths.sort(reverse=True)
        return [node for _, node in depths[:K]]

    removed = find_deepest_nodes(root)
    min_height = bfs(root, removed)

    return min_height

# Read input
N, K = map(int, input().split())
parent_list = list(map(int, input().split()))

# Calculate and print the minimum height
print(optimize_tree_height(N, K, parent_list))