class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        # sort the intervals
        intervals = sorted(intervals, key=lambda i: i[0])
        s, e = intervals[0][0], intervals[0][1]
        for cs, ce in intervals:
            # if the start is in the interval merge!
            if cs <= e:
                e = max(ce, e)
            else:
                out.append([s, e])
                s, e = cs, ce
        out.append([s, e])
        return out