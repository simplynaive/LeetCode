class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import collections
        d = collections.Counter(tasks)
        values = d.values()
        most = max(values)
        value_count = collections.Counter(values)
        return max((most - 1) * (n + 1) + value_count[most], len(tasks))


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(Solution().leastInterval(tasks, n))
