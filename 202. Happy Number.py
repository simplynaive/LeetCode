class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = 0
        seen = []
        while s != 1:
            nums = list(map(int, list(str(n))))
            s = 0
            for num in nums:
                s += num * num
                n = s
            if s in seen:
                return False
            seen.append(s)
            print(seen)
        return True


if __name__ == "__main__":
    n = 19
    print(Solution().isHappy(n))
