class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest_sequence = 0
        
        for num in hash_set:
            if (num - 1) not in hash_set:
                current = num
                curr_sequence = 0
                while True:
                    curr_sequence += 1
                    if (current + 1) in hash_set:
                        current += 1
                    else:
                        break

                if curr_sequence > longest_sequence:
                    longest_sequence = curr_sequence

        return longest_sequence