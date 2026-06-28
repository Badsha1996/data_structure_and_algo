
class Solution:
    def reverse(self, nums : list[int]) -> list[int]:
        # CODE HERE 
        i = 0
        j = len(nums) - 1

        while i < j:
            # Swap
            nums[i], nums[j] = nums[j], nums[i]

            i+=1
            j-=1

        return nums

if __name__=="__main__":
    arr : list[int] = [3,4,5,6,7,8]
    s : Solution = Solution()
    ans : list[int] = s.reverse(arr)

    # TIME - O(n)
    # SPACE - O(1)
    print(ans)
