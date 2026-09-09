class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the # of times the array has been rotated
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        rotations = l
        
        # now do binary search, but offset m by rotations
        length = len(nums)
        l, r = 0, length - 1
        while l <= r:
            m = (l + r) // 2
            val = nums[(m + rotations) % length]
            if val == target:
                return (m + rotations) % length
            elif val > target:
                r = m - 1
            else:
                l = m + 1
        return -1