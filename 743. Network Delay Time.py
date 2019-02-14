class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = [float("inf")] * (N + 1)

        def dfs(node, elapsed):
            if elapsed >= dist[node]:
                return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(K, 0)
        res = max(dist[1:])

        if res < float("inf"):
            return res
        return -1


if __name__ == "__main__":
    # times = [[3, 5, 78], [2, 1, 1], [1, 3, 0], [4, 3, 59], [5, 3, 85], [5, 2, 22], [2, 4, 23], [1, 4, 43], [4, 5, 75],
    #          [5, 1, 15], [1, 5, 91], [4, 1, 16], [3, 2, 98], [3, 4, 22], [5, 4, 31], [1, 2, 0], [2, 5, 4], [4, 2, 51],
    #          [3, 1, 36], [2, 3, 59]]
    # N = 5
    # K = 5

    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    N = 4
    K = 2
    print(Solution().networkDelayTime(times, N, K))
