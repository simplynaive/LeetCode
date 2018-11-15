import math


class Solution(object):
    # def countPrimes(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     self.prime = []
    #     count = 0
    #     for i in range(n):
    #         if self.isPrime(i):
    #             count += 1
    #             self.prime.append(i)
    #     print(self.prime)
    #     return count
    #
    # def isPrime(self, n):
    #     if n < 2:
    #         return False
    #     for i in range(len(self.prime)):
    #         if self.prime[i] * self.prime[i] <= n:
    #             if n % self.prime[i] == 0:
    #                 return False
    #         else:
    #             return True
    #     return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        is_prime = [True for _ in range(n)]
        is_prime[0], is_prime[1] = False, False
        for i in range(2, int(math.sqrt(n))+1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        return sum(is_prime)


if __name__ == "__main__":
    n = 100
    print(Solution().countPrimes(n))
