class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if not s:
        #     return ''
        # s = s.split(' ')
        # res = []
        # for i in range(len(s) - 1, -1, -1):
        #     if s[i]:
        #         res.append(s[i])
        # return ' '.join(res)

        if not s:
            return ''
        word = []
        res = []
        for i in range(len(s)):
            if s[i] != ' ':
                word.append(s[i])
                if i + 1 == len(s) or s[i + 1] == ' ':
                    res.append(''.join(word))
                    word = []
        i, j = 0, len(res) - 1
        while i < j:
            t = res[j]
            res[j] = res[i]
            res[i] = t
            i += 1
            j -= 1
        return ' '.join(res)


if __name__ == "__main__":
    s = "a good   example"
    print(Solution().reverseWords(s))