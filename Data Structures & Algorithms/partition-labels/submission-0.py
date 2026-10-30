from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = Counter(s)
        curr = set()
        out = []
        curr_count = 0
        for char in s:
            # if our current set is empty start a new set
            if not curr:
                counts[char] -= 1
                curr.add(char)
                curr_count += 1

            else:
                counts[char] -= 1
                curr.add(char)
                curr_count += 1

            for curr_char in curr:
                if counts[curr_char] > 0:
                    break
            else:
                curr.clear()
                out.append(curr_count)
                curr_count = 0
        return out