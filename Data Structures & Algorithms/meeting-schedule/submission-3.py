"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True 
        
        intervals.sort(key=lambda interval:interval.start)
        for i in range(1,len(intervals)):
            previous_interval = intervals[i -1]
            current_interval = intervals[i]
            if current_interval.start<previous_interval.end:
                return False 
        return True
