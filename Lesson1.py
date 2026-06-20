# Time Complexicity 
# Omega, Big O notaion, Theta Notation 
# BIG O ==> O(time)

# if a programe takes n time to execute then time complexicity will be - O(n)

# 10 --> 1 
# 1000 --> 1 * 1000
# TC - O(n) --> Linear realtionship 
# TC - O(1) --> Constant time 

data_set : int = 10  

for i in range(data_set):
    print(i+2)

# O(1) + O(n) = O(1+n) = O(n) beacuse 1 is negligable 

for i in range(data_set//2):
    print(i)

# O(n/2)

arr : list[int] = [1,2,3] # n  # O(1)
arr2 : list[int] = [1]    # m  # O(1)

arr3 : list[int] = arr + arr2  # O(1)

for ele in arr3:
    print(ele)

#O(m + n)


m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

row = len(m)
col = len(m[0])

for i in range(row):
    for j in range(col):
        print(m[i][j])

# O(1) + O(1) + O(1) = O(1) ===> constant 
# O(n)
# O(n)
# O(n * n) => O(n^2) 

for i in range(row):
    print(m[i])

# O(n)

for j in range(col):
    print(m[j])

# O(n) + O(n) = O(n)







