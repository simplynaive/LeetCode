# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        i = 1
        res = [intervals[0]]
        while i < len(intervals):
            if res[-1].end >= intervals[i].start:
                res[-1] = (Interval(res[-1].start, max(res[-1].end, intervals[i].end)))
                i += 1
            else:
                res.append(intervals[i])
                i += 1
        return res


if __name__ == "__main__":
    intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
    res = Solution().merge(intervals)
    for r in res:
        print(r.start, r.end)
