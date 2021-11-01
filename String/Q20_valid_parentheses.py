class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c = {'(': ')',
             '[': ']',
             '{': '}'}
        result = []
        for i in range(0, len(s)):
            if s[i] in c:
                result.append(s[i])
            else:
                if len(result) == 0:
                    return False
                if s[i] != c[result[-1]]:
                    return False
                else:
                    del result[-1]
        if len(result) == 1:
            return True
        else:
            return False

if __name__ == '__main__':
    print (Solution().isValid("()"))