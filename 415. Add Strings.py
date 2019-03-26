class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return None
        res = []
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0:
            n1 = n2 = 0

            if i >= 0 and num1[i]:
                n1 = ord(num1[i]) - ord('0')
            if j >= 0 and num2[j]:
                n2 = ord(num2[j]) - ord('0')

            temp = n1 + n2 + carry
            res.append(str(temp % 10))
            carry = temp // 10

            i -= 1
            j -= 1

        if carry:
            res.append(str(carry))

        return ''.join(reversed(res))


if __name__ == "__main__":
    s = '9133'
    t = '9'
    print(Solution().addStrings(s, t))

