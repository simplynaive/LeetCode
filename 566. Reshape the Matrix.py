class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        r_old = len(nums)
        c_old = len(nums[0])
        total = r_old * c_old
        if r * c != total:
            return nums
        res = []
        j = -1
        for i in range(total):
            if i == 0 and r == 1:
                res.append([])
                j += 1
            elif i % c == 0 and r != 1:
                res.append([])
                j += 1
            res[j].append(nums[i // c_old][i % c_old])
        return res


if __name__ == "__main__":
    nums = [[1, 2], [3, 4]]
    r = 4
    c = 1
    print(Solution().matrixReshape(nums, r, c))
