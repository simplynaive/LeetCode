# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start = newInterval.start
        end = newInterval.end
        res = []
        i = 0
        while i < len(intervals):
            if start <= intervals[i].end:
                if end < intervals[i].start:
                    break
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
            else:
                res.append(intervals[i])
            i += 1
        res.append(Interval(start, end))
        res += intervals[i:]
        return res


if __name__ == "__main__":
    intervals = [Interval(1, 5)]
    newInterval = Interval(6, 8)
    res = Solution().insert(intervals, newInterval)
    for r in res:
        print(r.start, r.end)
