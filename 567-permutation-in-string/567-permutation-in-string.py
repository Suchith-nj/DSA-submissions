class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dic = {}
        s2dic = {}
        if len(s2)<len(s1):
            return False
        for x in range (len(s1)):
            s1dic[s1[x]] = s1dic.get(s1[x],0) + 1
        for x in range (len(s1)):
            s2dic[s2[x]] = s2dic.get(s2[x],0) + 1
        
        l= 0
        if s1dic == s2dic:
            return True
        
        for r in range (len(s1), len(s2)):
            s2dic[s2[r]] = s2dic.get(s2[r],0) + 1
            s2dic[s2[l]]-=1
            if s2dic[s2[l]] == 0:
                s2dic.pop(s2[l])
            l+=1
            if s1dic == s2dic:
                return True
            
        return False
        
        
            
            
            
            
            