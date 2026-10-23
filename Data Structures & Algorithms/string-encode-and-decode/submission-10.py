class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for string in strs:
            out += (str(len(string)) + "#" + string)
        print(out)
        return out

    def decode(self, s: str) -> List[str]:
        num = ""
        out = []
        i = 0
        while i < len(s):
            if s[i] != "#":
                num +=s[i]
                i += 1
            else:
                out.append(s[i+1:i + int(num) + 1])
                i = i + int(num) + 1
                num = ""
        return out
        