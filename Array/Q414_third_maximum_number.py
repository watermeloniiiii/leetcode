class Solution():
    def solution1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        things pay attention to:
        1. when the length of the array is less than three, return the maxmium
        2. when are repeating elements
        3. the time complexity is O(n), we cannot use sorting
        """
        import numpy as np
        max1 = -2**31 - 1
        max2 = -2**31 - 1
        max3 = -2**31 - 1
        count = 0
        for i in range(len(nums)):
            flag = 0
            if nums[i] > max1:
                temp1 = nums[i]
                flag = 1
            if nums[i] < max1 and nums[i] > max2:
                temp2 = nums[i]
                flag = 2
            if nums[i] < max2 and nums[i] > max3:
                temp3 = nums[i]
                flag = 3
            ## replace the new maximum
            if flag == 1:
                max3 = max2
                max2 = max1
                max1 = temp1
                count += 1
            if flag == 2:
                max3 = max2
                max2 = temp2
                count += 1
            if flag == 3:
                max3 = temp3
                count += 1

        if count >= 3:
            return max3
        else:
            return np.maximum(max1, max2)

    def solution2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums is None:
            return

        n = list(set(nums))
        cp = n
        if len(n) <= 2:
            return max(n)
        else:
            i = 0
            while i < 2:
                cp.remove(max(cp))
                i += 1

        return max(cp)

if __name__ == '__main__':
    result = Solution().solution2([2, 2, 3, 1])
    print (result)