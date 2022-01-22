class Solution(object):
    def singleNumber(self, nums):
        from collections import Counter
        """
        :type nums: List[int]
        :rtype: int
        """
        # count = {}
        # for i in range(len(nums)):
        #     if nums[i] not in count:
        #         count[nums[i]] = 1
        #     else:
        #         del count[nums[i]]
        # return count.keys()[0]
        Z = Counter(nums)
        count = [i[1] for i in Z.items()]
        print (sorted(Z.items(), key = lambda kv:(kv[1], kv[0])))

if __name__ == '__main__':
    Solution().singleNumber([1,2,3,1,2,2])