class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """

        same number chose unlimited number of times

        base case:
        1. over target or i at end --> return
        2. == target --> add to path, return

        use (i)
        ~use (i+1)


        2 5 6 9

        """
        res = []

        path = []
        def dfs(i, path_sum):
            if i == len(nums) or path_sum > target:
                return
            if path_sum == target:
                res.append(path.copy())
                return
                
            
            
            # use it (i)
            path.append(nums[i])
            dfs(i, path_sum + nums[i])
            path.pop()
            # ~use it (i+1)
            dfs(i+1, path_sum)
        
        dfs(0, 0)
        return res

