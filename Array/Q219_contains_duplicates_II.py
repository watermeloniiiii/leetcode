class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        for i in range(len(nums) - k):
            p1 = 0
            p2 = 1
            subarray = nums[i:i+k+1]
            while p2 <= k:
                if subarray[p1] != subarray[p2]:
                    p2 += 1
                else:
                    return True
        return False

if __name__ == '__main__':
    print (Solution().containsNearbyDuplicate([99,99], 2))