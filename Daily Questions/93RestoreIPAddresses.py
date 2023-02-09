class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def rec(ind, ip):
            if ind == len(s) and len(ip) == 4:
                result.append('.'.join(ip))
                return
            elif ind == len(s) or len(ip) >= 4:
                return
            temp = s[ind]
            ip.append(temp)
            rec(ind+1, ip)
            ip.pop()
            if s[ind] != "0":
                if ind+1 < len(s):
                    temp += s[ind+1]
                    ip.append(temp)
                    rec(ind+2, ip)
                    ip.pop()
                if ind+2 < len(s):
                    temp += s[ind+2]
                    if temp <= "255":
                        ip.append(temp)
                        rec(ind+3, ip)
                        ip.pop()
        rec(0, [])
        return result