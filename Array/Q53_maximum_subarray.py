class Solution():
    def solution1(self, nums):
        subarray = 0
        for i in range(len(nums)):
            subarray = max(nums[i], subarray + nums[i])
        return subarray

if __name__ == '__main__':
    print (Solution().solution1([-2,1,-3,4,-1,2,1,-5,4]))