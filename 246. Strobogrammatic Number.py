class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num:
            return False
        if len(num) % 2 == 1:
            if num[len(num) // 2] not in '018':
                return False
        dic = [['0', '0'], ['1', '1'], ['8', '8'], ['6', '9'], ['9', '6']]
        i, j = 0, len(num) - 1
        while i < j:
            if [num[i], num[j]] not in dic:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    num = '659'
    print(Solution().isStrobogrammatic(num))
