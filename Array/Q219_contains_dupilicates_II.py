class Solution(object):
    def solution1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        '''
        Hashtable
        time complexity: O(m)
        space complexity: O(m)
        '''
        candidate = {}
        for i, ele in enumerate(nums):
            if ele in candidate and abs(i - candidate[ele]) <= k:
                return True
            candidate[ele] = i
        return False

    def solution2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

if __name__ == '__main__':
    print (Solution().solution1([1,0,1,1], 1))