class Solution:
    def compress(self, chars: List[str]) -> int:
        
        
        i = 0
        write = 0
        while i < len(chars):
            curr = chars[i]
            counter = 0            
            while i < len(chars) and chars[i] == curr:
                counter += 1
                i+=1
            chars[write] = curr
            write += 1 
            
                
            if counter > 1:
                for digit in str(counter):
                    chars[write] = digit
                    write += 1
        return write

