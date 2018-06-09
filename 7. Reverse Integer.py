class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return 0
        digits = []
        for d in str(x):
            digits.append(d)
        flag = 1
        if digits[0] == '-':
            flag = -1
            digits.remove('-')
        result = []
        for i in range(len(digits)):
            result.append(digits[len(digits) - 1 - i])
        reversed_num = 0
        for j in range(len(result)):
            reversed_num += int(result[j]) * pow(10, len(result) - 1 - j)
        if reversed_num * flag < -pow(2, 31) or reversed_num * flag > pow(2, 31) - 1:
            return 0
        return reversed_num * flag


def main():
    nums = 1534236469
    print(Solution().reverse(nums))


if __name__ == "__main__":
    main()