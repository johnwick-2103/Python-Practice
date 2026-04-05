class Solution:
    def sortPeople(self, names, heights):
        paired = list(zip(names, heights))
        
        paired.sort(key=lambda x: x[1], reverse=True)
        
        return [name for name, _ in paired]