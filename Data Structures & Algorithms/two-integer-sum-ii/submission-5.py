class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            complement = target - numbers[i]
            l = i + 1
            r = len(numbers)-1
            while l<=r:
                m = l + (r-l) // 2
                if numbers[m] == complement:
                    return [i+1,m+1]
                elif numbers[m] > complement:
                    r = m - 1
                else:
                    l = m + 1 