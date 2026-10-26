class Solution:
    def countSubstrings(self, s: str) -> int:
        # treat each char as the center of a palindrome, and count how many palindromes can be created with that character as its center
        out = 0
        for i in range(len(s)):
            # check for odd palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                out += 1
                l -= 1
                r += 1
            # check for even palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                out += 1
                l -= 1
                r += 1
        return out
