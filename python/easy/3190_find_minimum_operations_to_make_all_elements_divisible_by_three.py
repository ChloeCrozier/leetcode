# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            if n % 3 != 0:
                res += 1
        return res
