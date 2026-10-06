from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if s1 < s2 then return false
        # convert s1 into dictionary storing each character and its frequency
        # then initialize a window and slide it across s2 until the end of the window is larger than the length
        # keep a dictionary of the frequencies of all characters within the window and update it as it slides
        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])
        window_start = 0
        window_end = len(s1) - 1
        while True:
            print(s2_count)
            if s1_count == s2_count:
                return True
            window_start += 1
            window_end += 1
            if window_end == len(s2):
                return False
            s2_count[s2[window_end]] += 1
            s2_count[s2[window_start - 1]] -= 1
            if s2_count[s2[window_start - 1]] == 0:
                del s2_count[s2[window_start - 1]]
            