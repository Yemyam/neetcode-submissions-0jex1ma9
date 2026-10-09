class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0 
        for i, jump in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, jump + i)
        return True