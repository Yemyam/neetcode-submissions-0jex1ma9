"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda i: i.start)
        # store current meetings in a min heap, so the meeting ending at the earliest time is at the top
        meetings = []
        # keep a count of the max meetings that occur at once
        max_meetings = 0
        curr_meetings = 0
        for i in intervals:
            ms, me = i.start, i.end
            if meetings:
                while meetings and meetings[0] <= ms:
                    heapq.heappop(meetings)
                    curr_meetings -= 1

            heapq.heappush(meetings, me)
            curr_meetings += 1
            max_meetings = max(max_meetings, curr_meetings)

        return max_meetings


        