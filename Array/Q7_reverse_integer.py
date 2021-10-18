class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ## brutal solution
        # import numpy as np
        # target = 0
        # sign = x/np.abs(x)
        # str_list = str(np.abs(x))
        # l = len(str_list)
        # for i in range(0, l):
        #     target += int(str_list[-i-1])*10**(l-i-1)
        # if target < -2**31 or target > 2**31 -1:
        #     return 0
        # else:
        #     return target*sign
        ## pop
        rev = 0
        while x!=0:
            pop = x % 10
            x = x // 10
            rev = rev * 10 + pop




if __name__ == "__main__":
    solution = Solution()
    target = solution.reverse(353)