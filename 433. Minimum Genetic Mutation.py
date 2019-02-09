class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        queue = [(start, 0)]
        visited = set()
        while queue:
            word, dist = queue.pop(0)
            if word == end:
                return dist
            for i in range(len(word)):
                for j in 'ACGT':
                    tmp = word[:i] + j + word[i + 1:]
                    if tmp not in visited and tmp in bank:
                        queue.append((tmp, dist + 1))
                        visited.add(tmp)
        return -1


if __name__ == "__main__":
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA"]
    print(Solution().minMutation(start, end, bank))
