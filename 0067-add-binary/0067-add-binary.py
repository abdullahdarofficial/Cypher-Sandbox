class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        
        # sum_val = int(a, 2) + int(b, 2)

        # return bin(sum_val)[2:]


        result = []
        carry = 0

        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        for i in range(max_len - 1, - 1, -1):
            total = carry
            if a[i] == '1':
                total += 1
            if b[i] == '1':
                total += 1
            
            result.append(str(total % 2))
            carry = total // 2

        if carry:
            result.append("1")

        return "".join(reversed(result))

