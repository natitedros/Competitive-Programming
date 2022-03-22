class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        res = True
        for i in s:
            if i =="(" or i=="[" or i =="{":
                arr.append(i)
            elif len(arr)!=0 and (i == ")" or i == "]" or i == "}"):
                if arr[-1] == "(" and i ==")":
                    arr.pop()
                    
                elif arr[-1] == "[" and i =="]":
                    arr.pop()
                  
                elif arr[-1] == "{" and i == "}":
                    arr.pop()
                    
                else:
                    res = False
                    break
            else:
                res = False
                
                break
        if len(arr)!=0:
            res = False
        return res