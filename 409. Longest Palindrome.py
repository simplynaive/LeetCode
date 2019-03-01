class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnts = dict()
        for c in s:
            if c in cnts:
                cnts[c] += 1
            else:
                cnts[c] = 1
        l = 0
        odd = 0
        for c in cnts.keys():
            if cnts[c] % 2 != 0:
                odd = 1
            l += (cnts[c] // 2) * 2
        return l + odd


if __name__ == "__main__":
    s = "abccccdd"
    print(Solution().longestPalindrome(s))


# JAVA
# class Solution {
#     public int longestPalindrome(String s) {
#         int[] cnts = new int[256];
#         for (char c: s.toCharArray()){
#             cnts[c] ++;
#         }
#         int l = 0;
#         int odd = 0;
#         for (int c: cnts){
#             if (c % 2 != 0){
#                 odd = 1;
#             }
#             l += (c/2)*2;
#         }
#         return l + odd;
#     }
# }