# https://leetcode.com/problems/root-equals-sum-of-children/description/
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val
