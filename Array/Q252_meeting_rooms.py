class Solution():
    def canAttendMeetings(self, intervals):
        '''
        two python builtin functions:
        list.sort() inplace operation, only for list
        sorted() return values, for all iterable objects
        '''

        intervals = sorted(intervals, key=lambda interval: interval[0])
        prev = None
        for interval in intervals:
            if prev and interval[0] < prev[1]:
                return False
            prev = interval

        return True

if __name__ == '__main__':
    result = Solution().canAttendMeetings([[15,25], [5, 10], [20, 30]])
    print (result)