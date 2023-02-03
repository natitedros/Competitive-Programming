class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        stk = []
        ptr = 0
        while ptr < n:
            if path[ptr] == "/":
                ptr += 1
            else:
                buffer = ""
                while ptr < n and path[ptr] != "/":
                    buffer += path[ptr]
                    ptr += 1
                if buffer == ".." and stk:
                    stk.pop()
                elif buffer != ".." and buffer != ".":
                    stk.append(buffer)
        return "/"+"/".join(stk)