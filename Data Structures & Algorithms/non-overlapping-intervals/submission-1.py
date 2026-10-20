class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        out = 0
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = max(end, prevEnd)
            else:
                out += 1
                prevEnd = min(end, prevEnd)
        return out

