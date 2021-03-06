class Solution(object):
    def solution1(self, n):
        """
        :type n: int
        :rtype: int
        """
        # space complexity O(n)
        def climb(n):
            if n == 1: # only one step option is availble
                return 1
            if n == 2:  # two options are possible : to take two 1-stpes or to only take one 2-steps
                return 2
            return climb(n - 1) + climb(n - 2)

        return climb(n)
    #
    def solution2(self, n):
        memo = {}
        memo[1] = 1
        memo[2] = 2

        def climb(n):
            if n in memo:  # if the recurssion already done before first take a look-up in the look-up table
                return memo[n]
            else:  # Store the recurssion function in the look-up table and reuturn the stored look-up table function
                memo[n] = climb(n - 1) + climb(n - 2)
                return memo[n]
        return climb(n)

    def solution3(self, n):
        count = 0
        def recursive(cur):
            nonlocal count
            if cur > n:
                return
            if cur + 1 == n:
                count += 1
            elif cur + 2 == n:
                count += 2
            else:
                recursive(cur + 1)
                recursive(cur + 2)
        recursive(0)
        return count

if __name__ == '__main__':
    print (Solution().solution2(35))
    print (Solution().solution3(35))