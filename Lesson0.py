# What is Data ?
# Data is a collection of information

# How to store these data ?
# There arr multile ways to store Data, Those are called DATA STRCUTURE 

# There is a problem, how would you solve that problem ?
# There are multiple processes (step by step) to solve those problems. those 
# processes are called ALGORITHM


# Data structrue - 1 : List 
# Data structure - 2: String 
# Data structure - 3 : SET
# Data structure - 4 : Dictionary 

# **************************** LIST ****************************

num : list[int] = [1,2,3]
num.append(4) # add item to last 
num.pop()     # remove last item 
num.insert(0, 4) # add item in INDEX position 
num.remove(4)   # remove element
print(num)

# **************************** STRING ****************************

name = ""

name+="A"
name+="R"
name+="P"
name+="I"
name+="T"
name+="A"

name = name.replace("A", "I")

print(name[3:6]) # 4 = 4-1 > 3 index , 0 = srart from 0 index 
print(name[0:-2])
print(name[:-3]) # when we do not write anything it means 0

print(name[::-1]) # to reverse any string 


# **************************** DICT ****************************
freq : dict[str, int] = {} # optional : dict()

# I want to count the occurance of letter in name varible 

# freq["A"] = 90

# freq["A"] = freq.get("A", 0) + 1

for ch in name:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
print(freq.keys())
print(freq.values())
print(freq.items())

# **************************** SET ****************************

s : set[int] = set() # set() optional , {}

s.add(2)
s.add(3)
s.add(4)

s.remove(0)

print(45 in s)



