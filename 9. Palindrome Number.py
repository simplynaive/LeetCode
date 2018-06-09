
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        digits = []
        for d in str(x):
            digits.append(d)
        start,  end = 0, len(digits) - 1
        for i in range(len(digits)//2):
            if digits[start + i] != digits[end - i]:
                return False
        return True


def main():
    nums = 0
    print(Solution().isPalindrome(nums))


if __name__ == "__main__":
    main()