class Solution:
    def searchRange(self, nums, target):
        if nums == []:
            return [-1, -1]
        fast = 0
        slow = 0
        while fast < len(nums):
            if nums[fast] == target:
                nums[slow] = fast
                fast += 1
                slow += 1
            else:
                fast += 1
        if slow == 0 and nums[slow] != 0:
            return [nums[slow], nums[slow]]
        else:
            return [nums[0], nums[slow]]

if __name__ == '__main__':
    print (Solution().searchRange([5,7,7,8,8,10], 8))