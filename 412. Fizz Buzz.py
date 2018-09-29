class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for num in range(1, n + 1):
            if num % 15 == 0:
                res.append("FizzBuzz")
            elif num % 5 == 0:
                res.append("Buzz")
            elif num % 3 == 0:
                res.append("Fizz")
            else:
                res.append(str(num))
        return res


if __name__ == "__main__":
    n = 15
    print(Solution().fizzBuzz(n))
