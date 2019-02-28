class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) < 3:
            return len(s)

        l, r = 0, 0
        chars = dict()
        max_len = 2
        while r < len(s):
            if len(chars) < 3:
                chars[s[r]] = r
                r += 1

            if len(chars) == 3:
                delete = min(chars.values())
                del chars[s[delete]]
                l = delete + 1

            max_len = max(max_len, r - l)

        return max_len


if __name__ == "__main__":
    s = "eceba"
    print(Solution().lengthOfLongestSubstringTwoDistinct(s))

# JAVA
# class Solution {
# public int lengthOfLongestSubstringTwoDistinct(String s) {
# int n = s.length();
# if (n < 3){
#
#
# return n;
# }
#
# int
# l = 0;
# int
# r = 0;
#
# HashMap < Character, Integer > hashmap = new
# HashMap < Character, Integer > ();
# int
# max_len = 2;
#
# while (r < n){
# if (hashmap.size() < 3){
# hashmap.put(s.charAt(r), r++);
# }
#
# if (hashmap.size() == 3){
# int del_idx = Collections.min(hashmap.values());
# hashmap.remove(s.charAt(del_idx));
# l = del_idx + 1;
# }
#
# max_len = Math.max(max_len, r - l);
# }
# return max_len;
# }
# }