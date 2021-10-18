class Solution(object):
    def binarySearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ## time complexity O(log(n))
        strt = 0 #start index
        end = len(nums) - 1 #end index
        mid = 0 #stores the middle of the array
        while strt <= end:
            mid = strt + (end - strt)//2 #find middle of range of interest
            if target == nums[mid]:
                return mid
            if target < nums[mid]: #target can only be in the first half
                end = mid - 1 #adjust range to exclude the second half
            elif target > nums[mid]: #target can only be in the second half
                strt = mid + 1 #adjust range to exclude first half
        return strt #not in array, but start is intended index

    def bruteForce(self, nums, target):
        # time complexity: O(n)
        i = 0
        while nums[i] < target:
            i += 1
        return i


if __name__ == '__main__':
    result = Solution().bruteForce([1, 2, 5, 7, 9], 6)
    print (result)