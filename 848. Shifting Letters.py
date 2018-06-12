
class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        if len(S) != len(shifts) or not S:
            return None
        alphabeta = [chr(i) for i in range(97, 123)]
        S_list = list(S)
        result = []
        for i in range(len(S_list)):
            if shifts[i] > pow(10, 9):
                return None
            result.append(self.shift(S_list[i], sum(shifts[i:len(shifts)]), alphabeta))
        res = "".join(result)
        return res

    def shift(self, s, shifts, alphabeta):
        if not s:
            return
        if alphabeta.index(s) + shifts > 26:
            return alphabeta[alphabeta.index(s) + shifts - 26*((alphabeta.index(s) + shifts)//26)]
        else:
            return alphabeta[alphabeta.index(s) + shifts]

if __name__ == "__main__":
    S = 'bad'
    shifts = [10, 20, 30]
    print(Solution().shiftingLetters(S, shifts))
