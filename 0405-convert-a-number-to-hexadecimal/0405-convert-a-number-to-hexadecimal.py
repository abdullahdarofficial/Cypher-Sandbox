class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        
        hex_chars = []
        hex_map = "0123456789abcdef"

        if num < 0:
            num = (1<<32) + num

        while num > 0:
            remainder = num % 16
            hex_chars.append(hex_map[remainder])
            num //= 16

        hex_chars.reverse()
        return ''.join(hex_chars)