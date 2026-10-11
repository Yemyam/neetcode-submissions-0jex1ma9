"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key = lambda i: i.start)
        for i in range(1, len(intervals)):
            if sorted_intervals[i].start < sorted_intervals[i - 1].end:
                return False
        return True