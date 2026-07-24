# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        copies = dict()
        def dfs(curr: Optional['Node']):
            if curr in copies: return copies[curr]
            copy = Node(curr.val)
            copies[curr] = copy
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)
