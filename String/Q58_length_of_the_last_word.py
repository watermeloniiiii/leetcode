class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        fast, slow = 0, 0
        word = []
        s_len = len(s)
        s = s + ' '
        while fast < s_len:
            if s[slow] == ' ':
                slow += 1
                fast += 1
            if s[slow] != ' ' and s[fast] != ' ':
                fast += 1
            if s[slow] != ' ' and s[fast] == ' ':
                word.append(s[slow:fast])
                slow = fast
        return word

if __name__ == '__main__':
    Solution().lengthOfLastWord('hello worlds')