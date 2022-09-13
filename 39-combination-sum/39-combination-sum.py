class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curList, total):
            if total == target:
                res.append(curList.copy())
                return
            if i >= len(candidates) or total > target:
                return

            curList.append(candidates[i])
            #include candidate for sum
            dfs(i, curList, total + candidates[i])
            curList.pop()
            
            #don't include candidate for total
            #since we didn't add, we pass total without updating it
            dfs(i + 1, curList, total)

        dfs(0, [], 0)
        return res