class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashset = set()
        out = []
        for num in nums:
            hashset.add(num)
        for i in range(1, len(nums) + 1):
            if i not in hashset:
                out.append(i)

        return out