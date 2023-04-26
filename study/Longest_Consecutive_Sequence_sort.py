def LCS(nums):
    memo = {}
    total = 0
    nums.sort()

    for v in nums:
        memo[v] = 1
    
        
    return total
            

print(LCS([100,4,200,1,3,2]))
print(LCS([0,3,7,2,5,8,4,6,0,1]))