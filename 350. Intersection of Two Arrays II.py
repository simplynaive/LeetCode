class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = dict()
        res = []
        for n in nums1:
            d[n] = d.get(n, 0) + 1
        for m in nums2:
            if m in d.keys() and d[m] == 0:
                d.pop(m)
            if m in d.keys():
                d[m] -= 1
                res.append(m)
        return res


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(Solution().intersection(nums1, nums2))