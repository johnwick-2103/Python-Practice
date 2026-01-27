class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {}
        result = []
        min_sum = float('inf')

        for i, word in enumerate(list1):
            index_map[word] = i

        for j, word in enumerate(list2):
            if word in index_map:
                curr_sum = index_map[word] + j

                if curr_sum < min_sum:
                    min_sum = curr_sum
                    result = [word]
                elif curr_sum == min_sum:
                    result.append(word)

        return result
