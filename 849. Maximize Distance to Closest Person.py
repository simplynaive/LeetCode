class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        if not seats or not 1 <= len(seats) <= 20000:
            return None
        if min(seats) != 0 or max(seats) != 1:
            return None
        dist = []
        left, right = 0, 0
        flag = 0
        for j in range(len(seats)):
            if j != 0:
                if seats[j - 1] + seats[j] == 1:
                    flag += 1
        if seats[0] == 0 and seats[-1] == 0:
            method = max
        elif seats[-1] == 0 and flag < 4:
            method = max
        elif seats[0] == 0 and flag < 4:
            method = max
        else:
            method = min
        for i in range(len(seats)):
            if seats[i] == 0:
                j, k = i, i
                while j >= 0:
                    if seats[j] == 0:
                        j -= 1
                    else:
                        left = i - j
                        j = -1
                while k < len(seats):
                    if seats[k] == 0:
                        k += 1
                    else:
                        right = k - i
                        k = len(seats)
                dist.append(method(left, right))
        return dist


if __name__ == "__main__":
    seats = [0, 0, 1, 0, 1, 1]
    print(Solution().maxDistToClosest(seats))
