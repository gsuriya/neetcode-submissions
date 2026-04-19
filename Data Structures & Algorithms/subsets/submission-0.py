class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        path = []
        def dfs(i):
            if i == len(nums):
                res.append(path.copy())
                return
            
            # include
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            
            # ~include
            dfs(i+1)
        
        dfs(0)
        return res