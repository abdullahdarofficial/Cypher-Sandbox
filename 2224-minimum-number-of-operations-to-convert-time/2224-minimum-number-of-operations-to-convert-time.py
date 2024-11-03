class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        oper = 0
        currHr = int(current[:2])
        corrHr = int(correct[:2])
        currMn = int(current[3:])
        corrMn = int(correct[3:])
        print(currHr, corrHr, currMn, corrMn)
        diff = 0
        while currHr != corrHr:
            if currHr == (corrHr - 1) and currMn > corrMn:
                diff = 60 - currMn + corrMn
                break
            if currHr == 23:
                currHr == 0
            else:
                currHr += 1
            oper += 1
        
        if diff == 0:
            diff = corrMn - currMn
        val = 0
        while val != diff:
            if val + 15 <= diff:
                val += 15
            elif val + 5 <= diff:
                val += 5
            elif val + 1 <= diff:
                val += 1
            oper += 1
            
        return oper 

