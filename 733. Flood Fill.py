class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        color = image[sr][sc]
        if color == newColor:
            return image

        self.fill(sr, sc, image, color, newColor)

        return image

    def fill(self, i, j, image, color, newColor):
        if i < 0 or j < 0 or i > len(image) or j > len(image[0]):
            return

        image[i][j] = newColor

        if i - 1 >= 0 and image[i - 1][j] == color:
            image[i - 1][j] = newColor
            self.fill(i - 1, j, image, color, newColor)
        if i + 1 < len(image) and image[i + 1][j] == color:
            image[i + 1][j] = newColor
            self.fill(i + 1, j, image, color, newColor)
        if j - 1 >= 0 and image[i][j - 1] == color:
            image[i][j - 1] = newColor
            self.fill(i, j - 1, image, color, newColor)
        if j + 1 < len(image[0]) and image[i][j + 1] == color:
            image[i][j + 1] = newColor
            self.fill(i, j + 1, image, color, newColor)


if __name__ == "__main__":
    image = [[0, 0, 0], [0, 1, 0]]
    sr = 1
    sc = 1
    newColor = 2
    print(Solution().floodFill(image, sr, sc, newColor))
