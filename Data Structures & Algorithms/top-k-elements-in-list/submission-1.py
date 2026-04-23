from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        print(frequency)

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            frequency[c].append(n)

        out = []
        for i in range(len(frequency) -1, 0, -1):
            for n in frequency[i]:
                out.append(n)
                if len(out) == k:
                    return out
