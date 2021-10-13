class Solution():
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = nums[0]
        max2 = nums[0]
        max3 = nums[0]
        for i in range(len(nums)):
            if nums[i] > max1:
                max1 = nums[i]
            if nums[i] < max1 and nums[i] > max2:
                max2 = nums[i]
            if nums[i] < max2 and nums[i] > max3:
                max3 = nums[i]
        return max3

if __name__ == '__main__':
    result = Solution().thirdMax([3,2,1,5,7,6])
    print (result)