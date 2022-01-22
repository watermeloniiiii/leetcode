class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # new_list = []
        # slow, fast = 0, 0
        # s = s + ' '
        # while fast < len(s) - 1:
        #     if s[slow] == ' ':
        #         slow += 1
        #         fast += 1
        #     if s[slow] != ' ' and s[fast] != ' ':
        #         fast += 1
        #     if s[slow] != ' ' and s[fast] == ' ':
        #         new_list.append(s[slow:fast])
        #         slow = fast
        # def rev(l):
        #     left, right = 0, len(l) - 1
        #     while left <= right:
        #         l[left], l[right] = l[right], l[left]
        #         left += 1
        #         right -= 1
        #     return l
        # return rev(new_list)

        new_list = ' '.join(s.split(' ')[::-1])

        return new_list

if __name__ == '__main__':
    print(Solution().reverseWords('  the sky  is blue'))