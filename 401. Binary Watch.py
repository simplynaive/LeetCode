class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        leds = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]

        def dfs(leds, i, hr, mi, n):
            if n == 0:
                if mi < 10:
                    res.append(str(hr) + ':0' + str(mi))
                else:
                    res.append(str(hr) + ':' + str(mi))

            elif n > 0 and i < len(leds):
                if 0 <= i < 4 and hr + leds[i] < 12:
                    dfs(leds, i + 1, hr + leds[i], mi, n - 1)
                elif i > 3 and mi + leds[i] <= 59:
                    dfs(leds, i + 1, hr, mi + leds[i], n - 1)
                dfs(leds, i + 1, hr, mi, n)

        dfs(leds, 0, 0, 0, num)
        return res


if __name__ == "__main__":
    n = 5
    print(Solution().readBinaryWatch(n))
