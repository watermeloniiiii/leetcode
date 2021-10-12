class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import numpy as np
        import time
        start = time.time()
        ##         violent solution
        #         n = len(nums)
        #         for i in range(0, n):
        #             for j in range(i+1, n):
        #                 if nums[i] + nums[j] == target:
        #                     return [i, j]

        ##      hashtable
        #         n = len(nums)
        #         dic = {}
        #         for i in range(0, n):
        #             dic[i] = nums[i]
        #         for i in range(0, n):
        #             residual = target - nums[i]
        #             if residual in dic.values():
        #                 idx = list(dic.keys())[list(dic.values()).index(residual)]
        #                 if idx == i:
        #                     continue
        #                 else:
        #                     return [i, idx]

        keys = {}
        for i in range(len(nums)):
            if target - nums[i] in keys:
                return [keys[target - nums[i]], i]
            if nums[i] not in keys:
                keys[nums[i]] = i



if __name__ == "__main__":
    solution = Solution()
    target = solution.twoSum(range(0, 100), 28)
    print (target)
