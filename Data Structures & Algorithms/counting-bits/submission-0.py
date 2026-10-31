class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for num in range(n + 1):
            out.append(bin(num).count("1"))
        return out