# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
        
#         if root is None:
#             return 0
#         node = root
#         right = 1
#         while node.right:
#             right += 1
#             node = node.right

#         if node.left:
#             right += 1
#             return (2 ** right) - 2
#         else:
#             return (2 ** right) - 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        def leftDepth(node):
            depth = 1
            while node.left:
                depth += 1
                node = node.left
            
            return depth

        def rightDepth(node):
            depth = 1
            while node.right:
                depth += 1
                node = node.right
            
            return depth

        left = leftDepth(root)
        right = rightDepth(root)

        if right == left:
            return 2 ** left -1
        else:
            return 1 + self.countNodes(root.right) + self.countNodes(root.left)

