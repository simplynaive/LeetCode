class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        n_bin = str(bin(N))[2:]
        res = []
        for c in n_bin:
            if c == '1':
                res.append('0')
            else:
                res.append('1')
        return int(''.join(res), 2)


if __name__ == "__main__":
    N = 5
    print(Solution().bitwiseComplement(N))
