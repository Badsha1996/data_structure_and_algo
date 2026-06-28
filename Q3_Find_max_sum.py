
class Solution:
    def find_max_sum(self, nums: list[int]) -> int:
        # CODE HERE

        s = 0

        for i in range(len(nums)):
            if nums[i] > 0:
                s+=nums[i]

        return s

if __name__=="__main__":
    arr : list[int] = [3,-4,5,-16,7,-8]
    s : Solution = Solution()
    ans : int = s.find_max_sum(arr)

    # TIME - O(n)
    # SPACE - O(1)
    print(ans)
