class Solution(object):
    def solution1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)

    def solution2(self, nums, val):
        ## two pointer
        i = 0 ## slower pointer, move only when we do not encounter the target value
        for j in range(len(nums)): ## faster pointer
            if nums[j] != val: ## if the current element does not equal to the target value, store the value to the slower pointer
                nums[i] = nums[j]
                i += 1
        for delete_index in range(i, len(nums)):
            del nums[delete_index]
        return len(nums)

if __name__ == '__main__':
    print (Solution().solution2([0,1,2,3,4,5], 3))