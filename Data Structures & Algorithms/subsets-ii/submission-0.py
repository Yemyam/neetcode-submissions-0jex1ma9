class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # for each digit we can choose to include or exclude it
        # in order to avoid adding duplicate subsets we can sort the array of nums
        # we can either add the num, or not add it and skip all instances of that number
        out = []
        curr = []
        nums = sorted(nums)
        def backtrack(i, curr):
            if i >= len(nums):
                out.append(curr.copy())
                return
            curr.append(nums[i])
            backtrack(i + 1, curr)
            # skip all instances of num[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            curr.pop()
            backtrack(i + 1, curr)
        backtrack(0, curr)
        return out
            
