code = '''
def dfs(graph, start):
    visited = set()
    traversal_order = []

    def dfs_helper(vertex):
        visited.add(vertex)
        traversal_order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start)
    return traversal_order
'''
print(f"THIS IS THE MODIFIED CODE:")
print(convert_code_to_escaped_string(code))