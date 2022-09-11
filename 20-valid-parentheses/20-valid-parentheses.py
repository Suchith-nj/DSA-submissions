class Solution:
    def isValid(self, s: str) -> bool:
        # ({[{()}]})
        dic = {"{":"}", "[":"]", "(":")"}
        stack = []
        for x in range (len(s)):
            if s[x] in dic.keys():
                stack.append(s[x])
            elif stack and dic[stack[-1]] == s[x]:
                stack.pop()
            else:
                return False
        return True if len(stack)==0 else False
                