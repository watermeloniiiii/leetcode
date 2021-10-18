class Solution():
    def solution1(self, nums):

        s = [0 for i in range(len(nums))]
        s[0] = nums[0]
        for i in range(1, len(nums)):
            s[i] = max(nums[i], s[i-1]+nums[i])
        return max(s)

if __name__ == '__main__':
    print (Solution().solution1([-2,1]))