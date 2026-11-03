"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort the intervals based on their start time, then initalize a min heap which stores the end times of all meetings in progress
        # next we will iterate throught the list of meeting intervals and the end of each meeting that ended before the start of the current one will be popped
        # from the heap. Finally we will update the max size of the heap, since that is the max amount of meetings happening at the same time
        # we will return the max
        intervals = sorted(intervals, key = lambda i: i.start)
        heap = []
        max_rooms = 0
        for interval in intervals:
            m_s, m_e = interval.start, interval.end
            while heap and heap[0] <= m_s:
                heapq.heappop(heap)
            heapq.heappush(heap, m_e)
            max_rooms = max(max_rooms, len(heap))
        return max_rooms


        