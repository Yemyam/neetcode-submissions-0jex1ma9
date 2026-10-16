class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i, jump in enumerate(nums):
            if reach < i:
                return False
            reach = max(reach, i + jump)
        return True