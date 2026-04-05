class Solution:
    def sortPeople(self, names, heights):
        result = []
        
        for h in sorted(heights, reverse=True):
            index = heights.index(h)
            result.append(names[index])
        
        return result