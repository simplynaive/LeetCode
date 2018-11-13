class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for s in S:
            if s in J:
                count += 1
        return count


if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"
    print(Solution().numJewelsInStones(J, S))
