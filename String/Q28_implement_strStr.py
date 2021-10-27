class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) == 0 and len(needle) != 0:
            return -1
        if len(haystack) != 0 and len(needle) == 0:
            return -1
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        haystack = list(haystack)
        if len(needle) == 1:
            for i in range(len(haystack)):
                if haystack[i] == needle:
                    return i
            return -1
        else:
            for i in range(len(haystack)):
                if haystack[i:i+len(needle)] == needle:
                    return i
            return -1

if __name__ == '__main__':
    print (Solution().strStr("hello", "ll"))