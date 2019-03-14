class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        return len(s.split())


if __name__ == "__main__":
    s = "Hello, my name is John"
    print(Solution().countSegments(s))
