
class Solution:
    def find_max_index(self, nums: list[int]) -> int:
        max : int = 0
        maxi : int = -1

        n : int = len(nums)

        for i in range(n):
            if nums[i] > max:
                max = nums[i]
                maxi = i 

        return maxi 

if __name__=="__main__":
    arr : list[int] = [3,4,5,16,7,8]
    s : Solution = Solution()
    ans : int = s.find_max_index(arr)
    # SPACE - O(1)
    # TIME - O(n) # AVERAGE , WORST, BEST 
    print(ans)
