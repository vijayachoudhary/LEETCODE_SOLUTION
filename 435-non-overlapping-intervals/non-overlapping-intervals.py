class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        
        intervals.sort(key=lambda x:x[1])

        count = 0
        current_end = float('-inf')

        for start ,end in intervals:
            if start>=current_end:
                current_end = end
            else:
                count+=1

        return count            