class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        freqs = {}
        for r in range(len(s)):
            # win_size = r - l + 1
            freqs[s[r]] = 1 + freqs.get(s[r], 0)
            if (r - l + 1) - max(freqs.values()) <= k:
                max_len = max(max_len, r - l + 1)
            while (r - l + 1) - max(freqs.values()) > k:
                freqs[s[l]] -= 1
                l += 1
                
        return max_len
            
            