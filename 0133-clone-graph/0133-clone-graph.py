"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # if not node:
        #     return None
       
        # new_node = Node(node.val)
        # queue = deque([(node, new_node)])
        # visited = set()

        # while queue:
        #     old_curr, new_curr = queue.popleft()
        #     if old_curr not in visited:
        #         visited.add(old_curr)

        #         for neighbour in old_curr.neighbors:
        #             new_neighbor = Node(neighbour.val)
        #             new_curr.neighbors.append(new_neighbor)
        #             queue.append((neighbour, new_neighbor))

        # return new_node

        if not node:
            return None

        visited = {}

        new_node = Node(node.val)
        visited[node] = new_node

        queue = deque([node])

        while queue:
            old_curr = queue.popleft()

            for neighbor in old_curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                visited[old_curr].neighbors.append(visited[neighbor])

        return new_node