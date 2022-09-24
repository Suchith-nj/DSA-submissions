# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.pre = -math.inf
        self.res = math.inf

        def minDiffBST(root):
            if root is None:
                return

            minDiffBST(root.left)
            self.res = min(self.res, root.val - self.pre)
            self.pre = root.val

            minDiffBST(root.right)
            
        
        minDiffBST(root)
        return self.res
            