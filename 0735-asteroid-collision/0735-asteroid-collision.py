class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        # stack = []
        # for ast in asteroids:
        #     if len(stack) == 0:
        #         stack.append(ast)
        #     elif ast < 0 and stack[-1] > 0 or ast > 0 and stack[-1] < 0:
        #         if abs(ast) - abs(stack[-1]) > 0:
        #             # stack gone
        #             stack.pop()
        #             stack.append(ast)
        #         elif abs(ast) - abs(stack[-1]) == 0:
        #             stack.pop()
        #     else:
        #         stack.append(ast)

        # return stack
                
            
        stack = []
        for ast in asteroids:
            # Asteroids moving left can only collide with those moving right in the stack
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    # Top of the stack is destroyed, keep checking
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    # Both asteroids destroy each other
                    stack.pop()
                # If the asteroid in the stack is larger, current asteroid is destroyed
                break
            else:
                # No collision, add asteroid to the stack
                stack.append(ast)
                
        return stack