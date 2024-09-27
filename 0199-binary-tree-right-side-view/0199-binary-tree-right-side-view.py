# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # if not root:
        #     return []
        # out = []

        # out.append(root.val)
        # node = root
        # while node.right:
        #     out.append(node.right.val)
        #     node = node.right

        # return out


        if not root:
            return []

        queue = deque([root])
        out = []

        while queue:
            level_len = len(queue)
            for i in range(level_len):
                current = queue.popleft()
                if i == level_len - 1:
                    out.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return out

