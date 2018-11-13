class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        res.append(1)
        if n == 1:
            return res
        for i in range(1, n):
            print('------n =', i)
            last = list(map(int, str(res[i - 1])))
            print(last)
            cur = []
            l = 1
            label = [0]
            length = []
            value = []
            for j in range(len(last)):
                if j >= 1 and last[j - 1] != last[j]:
                    label.append(j)
            label.append(len(last))
            print('label', label)
            for k in range(len(label) - 1):
                length.append(label[k + 1] - label[k])
                value.append(last[label[k]])
            print('length', length)
            print('value', value)
            num = ''
            for a in range(len(length)):
                cur.append(length[a])
                cur.append(value[a])
                print('cur:', cur)
            for c in cur:
                num += str(c)
            print('cur:', num)
            res.append(int(num))
            print('res:', res)
        return res


if __name__ == "__main__":
    n = 5
    print(Solution().countAndSay(n))
