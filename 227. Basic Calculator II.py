class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return '0'
        num = 0
        res = []
        sign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == '+':
                    res.append(num)
                elif sign == '-':
                    res.append(-num)
                elif sign == '*':
                    res.append(res.pop() * num)
                else:
                    tmp = res.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        res.append(tmp // num + 1)
                    else:
                        res.append(tmp // num)
                num = 0
                sign = s[i]
        return sum(res)


if __name__ == "__main__":
    s = " 3+5 / 2 "
    print(Solution().calculate(s))
