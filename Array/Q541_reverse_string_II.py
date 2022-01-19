class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) < k:
            return s[::-1]
        s = list(s)
        def rev(s):
            left, right = 0, len(s) - 1
            while left <= right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            return s

        for i in range(0, len(s) - 1, 2 * k):
            if len(s[i:]) < k:
                break
            s[i:i + k] = rev(s[i:i + k])
        return ''.join(s)

if __name__ == '__main__':
    print (Solution().reverseStr('abcdefg',2))