class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # compute the prefix sum array
        prefix = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i - 1] + nums[i]
        
        curr_min = nums[0]
        curr_max = nums[0]

        for i in range(1, len(prefix)):
            curr_max = max(prefix[i], prefix[i] - curr_min, curr_max)
            if prefix[i] < curr_min:
                curr_min = prefix[i]
        return curr_max