class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        import numpy as np
        sorted_start = np.zeros(len(intervals))
        sorted_end = np.zeros(len(intervals))
        temp = 0
        for i in range(len(intervals)):
            if intervals[i][0] > temp:
                sorted_start[0] = intervals[i][0]
                sorted_end[0] = intervals[i][1]
                temp = intervals[i][0]
            else:
                sorted_start[i] = sorted_start[0]



if __name__ == '__main__':
    result1 = Solution().canAttendMeetings([[0, 6], [5, 20], [25, 50]])
    result2 = Solution().canAttendMeetings([[10, 20], [0, 6], [25, 50]])
    print (result1, result2)