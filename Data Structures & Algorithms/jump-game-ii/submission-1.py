class Solution:
    def jump(self, nums: List[int]) -> int:
        # start at the last index and work backwards?
        # we can reverse the array and work forward
        nums = nums[::-1]
        i = 0
        out = 0
        while i < len(nums) - 1:
            max_jump = 0
            for dist, jump in enumerate(nums[i + 1:]):
                dist += 1
                if jump >= dist:
                    max_jump = dist
            i += max_jump
            out += 1
        return out

