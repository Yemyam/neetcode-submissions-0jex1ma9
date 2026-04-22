from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        out = []
        sorted_nums = sorted(nums, key=nums_count.get, reverse=True)
        i = 0
        while k > 0:
            if sorted_nums[i] not in out:
                out.append(sorted_nums[i])
                k -= 1
            i += 1
        return out


