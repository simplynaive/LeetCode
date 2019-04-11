class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_dic = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for k in range(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if order_dic[word1[k]] > order_dic[word2[k]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False

        return True


if __name__ == "__main__":
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(Solution().isAlienSorted(words, order))
