from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # initalize a hashmap for t
        # move the left pointer once the correct window has been made
        t_map = Counter(t)
        curr_map = {}
        min_length = float("inf")
        out = ""
        l = 0
        for r in range(len(s)):
            curr_map[s[r]] = 1 + curr_map.get(s[r], 0)
            for key in t_map.keys():
                if not curr_map.get(key, 0) >= t_map[key]:
                    break
            # we can move the l pointer
            else:
                while True:
                    if s[l] not in t_map:
                        curr_map[s[l]] -= 1
                        l += 1
                    elif curr_map[s[l]] - 1 >= t_map[s[l]]:
                        curr_map[s[l]] -= 1
                        l += 1
                    else:
                        break
                length = r - l + 1
                if length < min_length:
                    out = s[l:r + 1]
                    min_length = length
        return out

