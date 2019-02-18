class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for d in digits:
            num = 10 * num + d
        num += 1
        return [int(n) for n in str(num)]


if __name__ == "__main__":
    s = [1, 2, 3]
    print(Solution().plusOne(s))
