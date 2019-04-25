class Solution(object):
    def calculate(self, s):
        res, num, sign, stack = 0, 0, 1, [1]
        for i in s + "+":
            if i.isdigit():
                num = 10 * num + int(i)
            elif i in "+-":
                res += num * sign * stack[-1]
                sign = 1 if i == "+" else -1
                num = 0
            elif i == "(":
                stack.append(sign * stack[-1])
                sign = 1
            elif i == ")":
                res += num * sign * stack[-1]
                num = 0
                stack.pop()
        return res


if __name__ == "__main__":
    s = "(1+(4+5+2)-3)+(6+8)"
    print(Solution().calculate(s))
