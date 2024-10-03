class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        # dire = 0
        # radiant = 0
        # flag = -1 # dire = 1 and radiant = 0
        # for char in senate:
        #     if char == "D":
        #         dire += 1
        #     elif char == 'R':
        #         radiant += 1
        #     if dire > radiant:
        #         flag = 1
        #     elif radiant > dire:
        #         flag = 0

        # if dire > radiant:
        #     return "Dire"
        # elif dire == radiant:
        #     if flag == 1:
        #         return "Dire"
        #     elif flag == 0:
        #         return "Radiant"
        # else:
        #     return "Radiant"

        queue = deque()
        for senator in senate:
            queue.append(senator)
        print(queue)
        flag = True
        killD = killR = 0
        while queue and flag:
            size = len(queue)
            for _ in range(size):
                senate = queue.popleft()
            
                if senate == 'D':
                    if killD > 0:
                        killD -= 1
                    else:
                        killR += 1
                        queue.append(senate)
                else:
                    if killR > 0:
                        killR -= 1
                    else:
                        killD += 1
                        queue.append(senate)
                        
            if size == len(queue):
                flag = False
        print(queue)
        if queue and queue[0] == 'R':
            return "Radiant"
        else:
            return "Dire"
            



