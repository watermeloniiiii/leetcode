class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        return sorted(nums1[:m] + nums2[:n])

if __name__ == '__main__':
    print (Solution().merge([1,2,3,0,0,0], 3, [4,5,6], 3))