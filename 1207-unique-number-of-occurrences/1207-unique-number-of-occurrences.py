class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        map = {}

        for num in arr:
            if num in map:
                map[num] = map[num] + 1
            else:
                map[num] = 1
        sets = set()
        for num, val in map.items():
            sets.add(val)
        
        if len(sets) == len(map):
            return True
        else:
            return False
            