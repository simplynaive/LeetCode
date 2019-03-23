# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        rooms = []
        m = 1
        for i in range(len(intervals)):
            if rooms and intervals[i].start >= min(rooms):
                rooms[rooms.index(min(rooms))] = intervals[i].end
            else:
                rooms.append(intervals[i].end)
            m = max(m, len(rooms))
        return m


if __name__ == "__main__":
    inputs = [[1293, 2986], [848, 3846], [4284, 5907], [4466, 4781], [518, 2918], [300, 5870]]
    intervals = []
    for input in inputs:
        intervals.append(Interval(input[0], input[1]))
    print(Solution().minMeetingRooms(intervals))
