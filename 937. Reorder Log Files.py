class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        if not logs:
            return []

        def competitor(log):
            iden, content = log.split(' ', 1)
            if content[0].isalpha():
                return 0, content, iden
            else:
                return 1,

        return sorted(logs, key=competitor)


if __name__ == "__main__":
    logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    print(Solution().reorderLogFiles(logs))
