class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        n = len(expression)

        def dfs(i):
            if expression[i] == 'T':
                if i + 1 < n and expression[i+1] == '?':
                    return dfs(i + 2)
                else:
                    return 'T'
            elif expression[i] == 'F':
                if i + 1 < n and expression[i+1] == '?':
                    index = i + 1
                    cnt = 1
                    while cnt > 0:
                        index += 1
                        if expression[index] == '?':
                            cnt += 1
                        if expression[index] == ':':
                            cnt -= 1
                    return dfs(index + 1)
                else:
                    return 'F'
            else:
                return expression[i]

        return dfs(0)


if __name__ == "__main__":
    s = "F?1:T?4:5"
    print(Solution().parseTernary(s))
