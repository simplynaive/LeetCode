class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if not points:
            return []

        def calc(elem):
            return elem[0]**2 + elem[1]**2
        points.sort(key=calc)
        return points[:K]


if __name__ == "__main__":
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    print(Solution().kClosest(points, K))

# # Java version
# class Solution {
#     public int[][] kClosest(int[][] points, int K) {
#         Arrays.sort(points, Comparator.comparing(p -> p[0]*p[0] + p[1]*p[1]));
#         return Arrays.copyOfRange(points, 0, K);
#     }
# }
