def convert_code_to_escaped_string(code):
    escaped_string = ""
    prev_space = 0
    for line in code.splitlines():
        stripped_line = line.lstrip()
        leading_spaces = len(line) - len(stripped_line)
        stripped_line = stripped_line.rstrip()
        
        if leading_spaces >= prev_space or leading_spaces == 0:
            escaped_string += '\n' + stripped_line\
        
        elif (prev_space > leading_spaces ):
            escaped_string += '\n' + ('\b' * (leading_spaces//4)) + stripped_line
        
        print(f'Line: {line}')
        print(f"leading_spaces {leading_spaces}")
        print(f"prev_spaces {prev_space}")

        # print(f"this was the stripped_line {stripped_line}")
        # print(f"this was the new line: {escaped_string}")
        print("")
        if leading_spaces == 0:
            prev_space = prev_space
        else:
            prev_space = leading_spaces
            
    return escaped_string

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

print(convert_code_to_escaped_string(code))


# problem: 
'''
if the previous space is the same or less then the cur_space:
    just do \n
elif 
'''
