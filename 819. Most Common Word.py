class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = "".join((char if char.isalpha() else " ") for char in paragraph.lower()).split()
        dic = dict()
        for para in paragraph:
            if para not in banned:
                if para in dic.keys():
                    dic[para] += 1
                else:
                    dic[para] = 1
        return max(dic, key=dic.get)


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit!"
    banned = ["hit"]
    print(Solution().mostCommonWord(paragraph, banned))
