class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        mapping = {}
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in mapping.keys() and mapping[pattern[i]] != words[i]:
                return False
            elif pattern[i] not in mapping.keys():
                if words[i] in mapping.values():
                    return False
                mapping[pattern[i]] = words[i]
        return True