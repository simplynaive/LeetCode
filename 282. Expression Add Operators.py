class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # Only +, -

        res = []

        def helper(num, temp, value, res):
            if not num:
                if value == target:
                    res.append(temp)
                return
            for i in range(1, len(num) + 1):
                val = num[:i]
                if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
                    helper(num[i:], temp + "+" + val, value + int(val), res)
                    helper(num[i:], temp + "-" + val, value - int(val), res)

        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
                helper(num[i:], num[:i], int(num[:i]), res)  # this step put first number in the string
        return res


if __name__ == "__main__":
    num = "1100"
    target = 0
    print(Solution().addOperators(num, target))
