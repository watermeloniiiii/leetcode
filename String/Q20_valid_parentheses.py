class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # c = {'(': ')',
        #      '[': ']',
        #      '{': '}'}
        # result = []
        # for i in range(0, len(s)):
        #     if s[i] in c:
        #         result.append(s[i])
        #     else:
        #         if len(result) == 0:
        #             return False
        #         if s[i] != c[result[-1]]:
        #             return False
        #         else:
        #             del result[-1]
        # return True
        if len(s) % 2 != 0:
            return False
        result = []
        for i in s:
            if i == '(':
                result.append(')')
            elif i == '[':
                result.append(']')
            elif i == '{':
                result.append('}')
            elif i == ')':
                paren = result.pop()
                if paren != i:
                    return False
            elif i == '}':
                if result.pop() != i:
                    return False
            elif i == ']':
                if result.pop() != i:
                    return False
        if len(result) != 0:
            return False
        return True
if __name__ == '__main__':
    print (Solution().isValid("()[]{}"))