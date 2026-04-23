class Solution:

    def encode(self, strs: List[str]) -> str:
        "é".join(strs)
        out = ""
        for string in strs:
            out += f"{string}é"
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        out_string = ""
        for char in s:
            if char != "é":
                out_string += char
            else:
                out.append(out_string)
                out_string = ""
        return out