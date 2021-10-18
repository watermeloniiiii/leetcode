import numpy as np

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_integer = {'I':1,
                         'V':5,
                         'X':10,
                         'L':50,
                         'C':100,
                         'D':500,
                         'M':1000}
        s_list = list(s)
        sum = 0
        sign = 1
        for i in range(0, len(s_list), 1):
            item = s_list[-1-i]
            if -1-i != -len(s_list):
                former_item = s_list[-1-i-1]
                if roman_integer[item] <= roman_integer[former_item]:
                    sum += roman_integer[item] * sign
                    sign = 1
                else:
                    sum += roman_integer[item]
                    sign = -1
            else:
                sum += roman_integer[item] * sign
        return sum

if __name__ == '__main__':
    solution = Solution()
    sum = solution.romanToInt('MCMXCIV')
    print (sum)
