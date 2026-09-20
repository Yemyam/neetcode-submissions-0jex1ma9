class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        chars = {}
        max_len = 0
        for r in range(len(s)):
            # window_len = r - l + 1
            chars[s[r]] = 1 + chars.get(s[r], 0)
            # while window len - most frequent char > k, increment l
            while (r - l + 1) - max(chars.values()) > k:
                chars[s[l]] -= 1
                l +=1
            max_len = max(max_len, r - l + 1)
        return max_len

            
            
            