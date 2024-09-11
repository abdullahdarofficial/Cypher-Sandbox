# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
#         self.result = False

#         def calculatePath(node, target, current):
#             print(current)
#             if node:
#                 if node.left is None and node.right is None:
#                     current += node.val
#                     if current == target:
#                         self.result = True
#                 else:

#                     current += node.val
#                     calculatePath(node.left, target, current)
#                     calculatePath(node.right,target, current)
#         curr = 0
#         calculatePath(root, targetSum, curr)
#         return self.result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        targetSum -= root.val
        return (self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum))
        