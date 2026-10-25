class Solution:
    def rob(self, nums: List[int]) -> int:
        # house robber 1 but we have 2 arrays one where we omit the first element, and one where we omit the last element, then we return the max of these two
        def robbing(houses):
            if len(houses) == 1:
                return houses[0]
            prevprev_best, prev_best = houses[0], max(houses[0], houses[1])
            i = 2
            while i < len(houses):
                curr_best = max(prev_best, prevprev_best + houses[i])
                prevprev_best = prev_best
                prev_best = curr_best
                i += 1
            return prev_best
        
        if len(nums) == 1:
            return nums[0]
        return max(robbing(nums[:-1]), robbing(nums[1:]))