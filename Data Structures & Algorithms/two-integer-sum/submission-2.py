class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mapping.keys():
                return [mapping[complement], i]
            else:
                mapping[nums[i]] = i
        