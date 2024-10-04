# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return 0
