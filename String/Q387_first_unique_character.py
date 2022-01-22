class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import  Counter
        z = Counter(s)
        candidate = [k for k in z.items() if k[1] == 1][0][0]

        return s.index(candidate)

if __name__ == '__main__':
    print (Solution().firstUniqChar('leetcode'))