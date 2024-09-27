# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        if not root:
            return []

        queue = deque([root])
        out = []

        reverse = False

        while queue:
            level_length = len(queue)
            semi = []
            temp = deque(queue)

            for i in range(level_length):
                if reverse:
                    tnode = temp.pop()
                else:
                    tnode = temp.popleft()

                semi.append(tnode.val)

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            out.append(semi)
            reverse = not reverse

        return out