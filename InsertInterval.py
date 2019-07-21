# -*- coding:utf-8 -*-
def insert(intervals, newInterval):
    # case 0 intervals is empty
    if len(intervals) == 0:
        return [newInterval]
    # case 1 intervals lie in the front
    if newInterval[1] < intervals[0][0]:
        intervals.insert(0, newInterval)
        return intervals
    # case 2 intervals lie in the front and merge
    if newInterval[1] == intervals[0][0]:
        intervals[0][0] = newInterval[0]
        return intervals
    # case 3  intervals lie in the back
    if newInterval[0] > intervals[-1][1]:
        intervals.append(newInterval)
        return intervals
    # case 4 intervals lie in the back and merge
    if newInterval[0] == intervals[-1][1]:
        intervals[-1][1] = newInterval[1]
        return intervals
    # write your code here
    for i in range(0, len(intervals) - 1):
        # case directly insert
        left = intervals[i][1]
        right = intervals[i + 1][0]
        if newInterval[0] > left and newInterval[1] < right:
            intervals.insert(i + 1, newInterval)
            return intervals
        if newInterval[0] == left and newInterval[1] == right:
            intervals[i + 1][0] = intervals[i][0]
            intervals.pop(i)
            return intervals
        if newInterval[0] == left and newInterval[1] < right:
            intervals[i][1] = newInterval[1]
            return intervals
        if newInterval[0] > left and newInterval[1] == right:
            intervals[i + 1][0] = newInterval[0]
            return intervals

print insert([[1,2], [5,9]],[2,5]);
