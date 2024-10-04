# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return root

        queue = deque([root])
        maxsum = float("-inf")

        maxlevel = 0
        currlevel = 1
        while queue:
            size = len(queue)
            currsum = 0
            for _ in range(size):
                node = queue.popleft()
                currsum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if maxsum < currsum:
                maxsum = currsum
                maxlevel = currlevel
            currlevel += 1

        return maxlevel    