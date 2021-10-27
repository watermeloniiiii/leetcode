class Solution(object):

    def solution1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        for i in range(0, len(nums) - 1):
            ## if the later element equals to its former, we remove it but keep the index, becuase we have removed one element
            ## next time we will evaluate the element at the same position (but has been updated to its next value)
            if nums[i+1] == nums[i]:
                nums.remove(nums[i+1])



        return len(nums)

    def solution2(self, nums):

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        j = 1  # slower pointer, only move when meet unique number
        for i in range(1, len(nums)):  # faster pointer, i will iterate over all element in nums
            if nums[i] != nums[i - 1]:  # when nums[i] is a unique number, assign it to nums[j]
                nums[j] = nums[i]
                j += 1

        # After for loop, i = 9, j = 5, nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
        # We have to delete duplicates backwards
        for delete_index in range(i, j - 1, -1):
            del nums[delete_index]

        return j

if __name__ == '__main__':
    print(Solution().solution1([0,0,1,1,1,2,2,3,3,4]))