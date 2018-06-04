import time

def repeatedStringMatch(A, B):
    """
    :type A: str
    :type B: str
    :rtype: int
    """
    if not A or not B:
        return -1
    for i in range(len(B)//len(A), len(B)//len(A)+3):
        if B in A*i:
            return i
    return -1


def main():
    A = "abababaaba"
    B = "aabaaba"
    start = time.time()
    print(repeatedStringMatch(A, B))
    end = time.time()
    print("runtime = ", end - start)

if __name__ == "__main__":
    main()