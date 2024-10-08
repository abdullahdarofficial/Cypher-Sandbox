# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        

        self.tree = []

        def getTrees(node):
            if node:
                getTrees(node.left)
                getTrees(node.right)
                if node.left is None and node.right is None:
                    self.tree.append(node.val)
        getTrees(root1)
        tree1 = list(self.tree)
        print(self.tree)
        self.tree.clear()
        print(self.tree)
        getTrees(root2)
        tree2 = self.tree
        print(self.tree)


        print(tree1, tree2)
        if tree1 == tree2:
            return True
        else:
            return False
