class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        #sort to skip the duplicates if any
        nums.sort()
        

        def backtrack(i, subset):
            if i == len(nums):
                result.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            
            # All subsets that don't include nums[i] #we dont append here
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1          #skip if duplicates
            backtrack(i + 1, subset)

        backtrack(0, [])
        return result