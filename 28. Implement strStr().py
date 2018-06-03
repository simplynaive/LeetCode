
def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(needle) == 0:
        return 0
    if len(haystack) == 0 or len(needle) > len(haystack):
        return -1
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i] == needle[0]:
            if i+len(needle) > len(haystack):
                break
            elif haystack[i:i+len(needle)] == needle:
                return i
    return -1


def main():
    haystack = "a"
    needle = "a"
    print(strStr(haystack, needle))


if __name__ == "__main__":
    main()