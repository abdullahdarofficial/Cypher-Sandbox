# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        def calculate_average_levels(node, sums, level):
            if node:
                if level in sums:
                    current_sum, count = sums[level] 
                else:
                    current_sum = count = 0

                current_sum += node.val
                count += 1

                sums[level] = (current_sum, count)

                calculate_average_levels(node.left, sums, level + 1)
                calculate_average_levels(node.right, sums, level + 1)

        self.map = {}
        calculate_average_levels(root, self.map, 0)

        return [sum / count for sum, count in self.map.values()]


            
