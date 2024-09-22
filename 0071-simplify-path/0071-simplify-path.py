class Solution:
    def simplifyPath(self, path: str) -> str:
        # if not path: 
        #     return path

        # new_str = []
        # new_str.append('/')
        # index = 0
        # i = 0
        # while i < len(path):
        #     if path[i] == '/' and new_str[index] == '/':
        #         i += 1
        #         continue
        #     elif path[i] == '/' and new_str[index] != '/':
        #         new_str.append('/')
        #         index += 1
        #         i += 1
        #     elif path[i] == ".":
        #         if i + 1 < len(path) and path[i + 1] == '.' :
        #             if i + 2 < len(path) and path[i+2] == '.':
        #                 while i < len(path) and path[i] =='.':
        #                     new_str.append('.')
        #                     i+= 1
        #                     index += 1
        #             new_str.pop()
        #             index -= 1
        #             while index >= 0 and new_str[index] != "/":
        #                 new_str.pop()
        #                 index -= 1
        #     else:
        #         new_str.append(path[i])
        #         i += 1
        #         index += 1


        # if new_str[index] == '/':
        #     new_str.pop()
        # return new_str

        if not path:
            return path

        stack = []

        components = path.split('/')

        for component in components:
            if component == '' or component == '.':
                continue
            elif component == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(component)

        return '/' + '/'.join(stack)