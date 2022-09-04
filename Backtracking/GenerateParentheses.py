class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(opens,closes,stk,par):
            if not opens and not closes:
                if not stk:
                    res.append(par)
                return
            elif not closes:
                return 
            elif not opens:
                if stk: stk.pop()
                else: return
                dfs(opens,closes-1,stk,par+')')
            else:
                dfs(opens-1,closes,stk+['('],par+'(')
                if stk: stk.pop()
                else:   return
                dfs(opens,closes-1,stk,par+')')
        dfs(n,n,[],'')
        return res   