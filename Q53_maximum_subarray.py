class Solution(object):
    def solution1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negative_index = []
        for i in range(len(nums) - 1):
            if nums[i] < 0:
                negative_index.append(i)
        if len(negative_index) == 0:
            return sum(nums)
        if len(negative_index) == 1:
            return max(sum(nums[:negative_index[0]]), sum(nums), sum(nums[negative_index[0]+1:]))


        subarray = []
        break_point = 0
        for n_i in range(len(negative_index)-1):
            test = sum(nums[break_point:negative_index[n_i] + 1])
            if sum(nums[break_point:negative_index[n_i] + 1]) >= 0:
                subarray += nums[break_point + 1:negative_index[n_i + 1]]
            else:
                break_point = negative_index[n_i]
        return sum(subarray)

    def solution2(self, nums):
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        return max(dp)




if __name__ == '__main__':
    result = Solution().solution2([5, -6, 3, 2, -7, 1, 2, 4])
    print (result)
