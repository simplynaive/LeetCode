class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        l, r = 0, len(height) - 1
        maxLeft = height[0]
        maxRight = height[-1]
        res = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] > maxLeft:
                    maxLeft = height[l]
                else:
                    res += maxLeft - height[l]
                l += 1
            else:
                if height[r] > maxRight:
                    maxRight = height[r]
                else:
                    res += maxRight - height[r]
                r -= 1
        return res


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))
