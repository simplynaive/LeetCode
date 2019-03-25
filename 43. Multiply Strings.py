class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            carry = 0
            for j in range(len(num2) - 1, -1, -1):
                temp = int(num1[i]) * int(num2[j]) + carry
                carry = (res[i + j + 1] + temp) // 10
                res[i + j + 1] = (res[i + j + 1] + temp) % 10
                print(res)
            res[i] += carry
        if sum(res) == 0:
            return 0
        res = ''.join(map(str, res))
        return res.lstrip('0')


if __name__ == "__main__":
    num1 = "232"
    num2 = "53"
    print(Solution().multiply(num1, num2))
