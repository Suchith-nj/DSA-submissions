class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sdic = {}
        tdic = {}
        res = ""
        
        if len(s)<len(t) or t =="":
            return ""
        
        for x in range (len(t)):
            tdic[t[x]] = tdic.get(t[x],0) + 1
            
        have , need = 0, len(tdic)
        l= 0
        resLen = math.inf
        
        for r in range (len(s)):
            sdic[s[r]] = sdic.get(s[r],0) + 1
            
            if s[r] in tdic and sdic[s[r]] == tdic[s[r]]:
                have += 1
                
            while have == need:
                if (r-l+1)< resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                
                sdic[s[l]]-=1
                if s[l] in tdic and sdic[s[l]]<tdic[s[l]]:
                    have -=1
                l+=1
        
        return res
                
            
        
            
            
            
            
            