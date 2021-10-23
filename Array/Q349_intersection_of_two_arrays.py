class Solution(object):
    def solution1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        if len(nums1) < len(nums2):
            return [x for x in nums1 if x in nums2]
        else:
            return [x for x in nums2 if x in nums1]

if __name__ == '__main__':
    print (Solution().solution1([1,2,3,4], [2,3]))
