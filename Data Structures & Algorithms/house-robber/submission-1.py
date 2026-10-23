class Solution:
    def rob(self, nums: List[int]) -> int:
        # we can create an array of the max amout that can be robbed upto a certain index
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        maxxes = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            maxxes.append(max(maxxes[i-2] + nums[i], maxxes[i - 1]))
        print(maxxes)
        return max(maxxes[-1], maxxes[-2])
        