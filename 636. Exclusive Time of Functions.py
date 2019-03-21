class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        curr = []
        start_time = 0
        for log in logs:
            i, flag, t = log.split(':')
            i = int(i)
            t = int(t)
            if flag == 'start':
                if curr:
                    res[curr[-1]] += t - start_time - 1
                curr.append(i)
                start_time = t
            else:
                res[curr.pop()] += t - start_time + 1
                start_time = t
        return res


if __name__ == "__main__":
    n = 2
    logs = ["0:start:0",
            "1:start:2",
            "1:end:5",
            "0:end:6"]
    print(Solution().exclusiveTime(n, logs))
