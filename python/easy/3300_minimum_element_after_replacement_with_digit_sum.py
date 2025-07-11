# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/
class Solution:
    def minElement(self, nums: List[int]) -> int:
        minVal = 46
        for n in nums:
            minVal = min(minVal, sum(int(x) for x in str(n)))
        return minVal
