class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        idx = 0
        output = [-1, -1]
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        while start <= end:
            mid = start + (end - start) // 2
            if target < nums[mid]:
                end = mid - 1
            if target > nums[mid]:
                start = mid + 1
            if target == nums[mid]:
                output[idx] = mid
                idx = 1
                if mid == start:
                    start = mid + 1
                elif target < nums[mid + 1]:
                    end = mid - 1
                elif target > nums[mid - 1]:
                    start = mid + 1
        output.sort()
        test = output[0] * output[1]
        if -1 in output:
            return [output[1], output[1]]

        return output

if __name__ == '__main__':
    result1 = Solution().searchRange([1,3], 1)
    print (result1)