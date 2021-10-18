class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        import numpy as np
        sign = x / np.abs(x)
        if sign < 0:
            return 'false'
        l = []
        while x != 0:
            pop = x % 10
            x //= 10
            l.append(pop)
        middle = int(np.round((len(l)-1) / 2))
        first_half = l[:middle]
        second_half = l[middle:]
        second_half.reverse()
        if first_half == second_half:
            return 'true'
        else:
            return 'false'

if __name__ == "__main__":
    solution = Solution()
    target = solution.isPalindrome(123)
    print (target)