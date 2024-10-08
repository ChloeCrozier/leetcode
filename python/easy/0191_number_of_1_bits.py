# https://leetcode.com/problems/number-of-1-bits/description/
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        index = 1
        while n:
            if n & 1:
                count += 1
            n = n >> 1
        return count
