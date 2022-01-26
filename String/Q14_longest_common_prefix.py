class Solution:
    def longestCommonPrefix(self, strs):
        strs = sorted(strs, key=lambda l: len(l))  ## nlog(n)
        if strs[0] == '':
            return ''
        flag = 0
        j = 0
        while j < len(strs[0]):
            for i in range(0, len(strs)):
                if strs[i][:j + 1] != strs[0][:j + 1]:
                    flag = 1
                    break

            if flag == 1:
                break
            j += 1
        if j == 0:
            return ''
        else:
            return strs[0][:j]

if __name__ == '__main__':
    print (Solution().longestCommonPrefix(
["a"]))
