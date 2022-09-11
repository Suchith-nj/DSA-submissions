# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def gn(root, maxUntil):
            if not root:
                return 0
            
            if root.val >= maxUntil:
                res =1
            else:
                res = 0
                
            maxUntil = max(root.val, maxUntil)
            
            res += gn(root.left, maxUntil) + gn(root.right, maxUntil)
            
            
            return res
        
        result = gn(root, -math.inf)
        return result