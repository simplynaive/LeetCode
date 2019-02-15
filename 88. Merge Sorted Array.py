class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[:m]
        nums1[:] = []
        i, j = 0, 0
        while i < m and j < n:
            if nums3[i] > nums2[j]:
                nums1.append(nums2[j])
                j += 1
            else:
                nums1.append(nums3[i])
                i += 1
        if i < m:
            nums1[i + j:] = nums3[i:]
        if j < n:
            nums1[i + j:] = nums2[j:]
        print(nums1)


if __name__ == "__main__":
    nums1 = [4, 0, 0, 0, 0, 0]
    m = 1
    nums2 = [1, 2, 3, 5, 6]
    n = 5
    # nums1 = [1, 2, 3, 0, 0, 0]
    # m = 3
    # nums2 = [2, 5, 6]
    # n = 3
    print(Solution().merge(nums1, m, nums2, n))
