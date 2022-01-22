class Solution(object):
    def solution1(self, s):
        ## O(m)
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)):
            ## step 1 determine if the s[:i+1] equals s[i + 1:2 * (i + 1)]
            ## if not, then move i to its next
            if s[:i + 1] != s[i + 1:2 * (i + 1)]:
                i += 1
            elif len(s) % len(s[:i + 1]) != 0:
                continue
            elif len(s) % len(s[:i + 1]) == 0:
                if s == s[:i + 1] * (len(s) // len(s[:i + 1])):
                    return True
                else:
                    continue
        return False

    def solution2(self, s):
        ## O(m)
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s) - 1):
            ## step 1 determine if the s[:i+1] equals s[i + 1:2 * (i + 1)]
            ## if not, then move i to its next
            if s == s[:i+1] * (len(s) // len(s[:i+1])):
                return True
            else:
                continue
        return False

if __name__ == '__main__':
    print (Solution().solution2('aba'))