class Solution:
    def rob(self, nums: List[int]) -> int:
        # track prev_best and prevprev_best
        if len(nums) == 1:
            return nums[0]
        prevprev_best = nums[0]
        prev_best = max(nums[0], nums[1])
        i = 2
        while i < len(nums):
            curr_best = max(prevprev_best + nums[i], prev_best)
            prevprev_best = prev_best
            prev_best = curr_best
            i += 1
        return prev_best
        