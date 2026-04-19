class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """

        9 2 2 4 6 1 5

          i
        1 2 2 4 5 6 9 3

        sort
        use it (i+1)
        ~use it (i skip dups)

        """
        candidates.sort()
        res = []

        path = []
        def dfs(i, path_sum):
            if path_sum == target:
                res.append(path[:])
                return
            
            if i == len(candidates) or path_sum > target:
                return
            
            # use it (i+1)
            path.append(candidates[i])
            dfs(i+1, path_sum + candidates[i])
            path.pop()
            
            # ~use it (i skip dups)
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            i += 1
            dfs(i, path_sum)

        dfs(0, 0)
        return res



