class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ""
        max_length = 0
        for i in range(len(s)):
            # check of odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > max_length:
                    max_length = length
                    out = s[l:r + 1]
                l -= 1
                r += 1
            # check of even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > max_length:
                    max_length = length
                    out = s[l:r + 1]
                l -= 1
                r += 1
        return out