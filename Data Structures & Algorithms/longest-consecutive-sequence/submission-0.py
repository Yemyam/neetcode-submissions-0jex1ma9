class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}
        longest_sequence = 0
        # Create num hash_map
        for num in nums:
            if num not in hash_map.keys():
                hash_map[num] = True
        
        for num in nums:
            if (num - 1) not in hash_map.keys():
                current = num
                curr_sequence = 0
                while True:
                    curr_sequence += 1
                    if (current + 1) in hash_map.keys():
                        current += 1
                    else:
                        break

                if curr_sequence > longest_sequence:
                    longest_sequence = curr_sequence

        return longest_sequence