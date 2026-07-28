class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for string in strs:
            out += str(len(string)) + "#" + string
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        index = 0
        while index < len(s):
            j = s.index("#", index)
            length = int(s[index:j])
            out.append(s[j+1: j+1+length])
            index = j + 1 + length
        return out