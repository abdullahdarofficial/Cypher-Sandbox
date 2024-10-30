class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        index = 0
        keys = set()
        maxTime = releaseTimes[index]
        keys.add(keysPressed[index])
        for i in range(1, len(releaseTimes)):
            if (releaseTimes[i] - releaseTimes[i-1]) > maxTime:
                maxTime = (releaseTimes[i] - releaseTimes[i-1])
                keys.clear()
                keys.add(keysPressed[i])
            elif (releaseTimes[i] - releaseTimes[i-1]) == maxTime:
                keys.add(keysPressed[i])
            print(keys)

        return max(keys) if keys else ''