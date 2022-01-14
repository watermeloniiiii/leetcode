class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        fast = 0
        slow = 0
        l = float('inf')
        while fast < len(nums):
            if sum(nums[slow:fast + 1]) < target:
                fast += 1
            if sum(nums[slow:fast + 1]) >= target:
                if fast - slow + 1 < l:
                    l = fast - slow + 1
                slow += 1
        return l

if __name__ == '__main__':
    print (Solution().minSubArrayLen(6, [10,2,3]))