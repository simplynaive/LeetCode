class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars or len(chars) == 0:
            return []

        start = i = 0
        while i < len(chars):
            char = chars[i]
            length = 1
            while i + 1 < len(chars) and char == chars[i + 1]:
                length += 1
                i += 1
            if length > 1:
                len_str = str(length)
                chars[start + 1: start + 1 + len(len_str)] = len_str
                start += len(len_str)
            start += 1
            i += 1
        return start

        # start = 0
        # index = 0
        # for i in range(1, len(chars)):
        #     if chars[i] != chars[i - 1]:
        #         chars[index] = chars[i - 1]
        #         index += 1
        #         insert = str(i - start)
        #         if i - start > 1:
        #             chars[index: index + len(insert)] = insert
        #             index += len(insert)
        #         start = i
        #     if i == len(chars) - 1:
        #         chars[index] = chars[i]
        #         index += 1
        #         insert = str(i - start)
        #         if i - start > 1:
        #             chars[index: index + len(insert)] = insert
        #             index += len(insert)
        #         start = i
        # return chars


if __name__ == "__main__":
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c", "c"]
    print(Solution().compress(chars))
