class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp = []
        out = []
        for i in range(len(names)):
            temp.append([heights[i], names[i]])
        temp.sort(reverse = True)
        for t in temp:
            out.append(t[1])
        return out