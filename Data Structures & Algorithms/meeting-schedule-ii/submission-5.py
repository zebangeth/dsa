"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            start, end = interval.start, interval.end
            events.append((start, 1))
            events.append((end, -1))
        
        events.sort()
        rooms = 0
        max_rooms = 0
        for event in events:
            rooms += event[1]
            max_rooms = max(rooms, max_rooms)
        return max_rooms
