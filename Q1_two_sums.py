class Solution(object):
    def unordered(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        keys = {}
        for i in range(len(nums)):
            if target - nums[i] in keys:
                return [keys[target - nums[i]], i]
            if nums[i] not in keys:
                keys[nums[i]] = i

    def ordered(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        keys = {}
        for i in range(len(nums)):
            if target - nums[i] in keys:
                return [i, keys[target - nums[i]]]
            if nums[i] not in keys:
                keys[nums[i]] = i


if __name__ == "__main__":
    target = Solution.ordered(range(0, 100), 28)
    print (target)
