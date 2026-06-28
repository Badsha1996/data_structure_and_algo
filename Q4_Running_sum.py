
class Solution:
    def running_sum(self, nums: list[int]) -> list[int]:
        # CODE HERE
        # APPROCH - 1
        # new : list[int] = []

        # n = len(nums)
        # for i in range(n):
        #     total = 0
        #     for j in range(i, -1, -1):
        #         total += nums[j]
        #     new.append(total)

        # return new

        # APPROCH - 2
        # new = [] # 2 , 6, 12, 20
        # total = 0 # 20
        # n = len(nums)

        # for i in range(n):
        #     total+=nums[i] 
        #     new.append(total)

        # return new 

        # APPROCH - 3
        n = len(nums)
        for i in range(1, n):
            nums[i] = nums[i] + nums[i-1]
        return nums





if __name__=="__main__":
    arr : list[int] = [2,4,6,8] # [2 , 6 , 12 , 20]
    s : Solution = Solution()
    ans : list[int] = s.running_sum(arr)

    # APPROCH - 1
    # TIME - O(n^2)
    # SPACE - O(n)

    # APPROCH - 2
    # TIME - O(n)
    # SPACE - O(n)

    # APPROCH - 3
    # TIME - O(n)
    # SPACE - O(1)

    print(ans)
