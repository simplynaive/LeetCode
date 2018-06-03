def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
        return False
    for i in range(int(len(s)/2) + 1):
        substr = s[0:i + 1]
        n = 1
        while i + (i + 1) * n < len(s):
            if s[(i + 1) * n: i + (i + 1) * n + 1] == substr:
                if i + (i + 1) * n == len(s) - 1:
                    return True
                n += 1
            else:
                break
    return False


def main():
    s = "abab"
    print(repeatedSubstringPattern(s))


if __name__ == "__main__":
    main()