def longestConsecutinve(nums):
    num_dict = {}
    longest = 0

    for num in nums:
        num_dict[num] = 1
    
    for num in nums:
        count = 0
        time = num
        prev = num - 1
        if prev not in num_dict:
            while time in num_dict:
                time += 1
                count += 1
                if longest < count:
                    longest = count
        
    return longest
            

print(longestConsecutinve([100,4,200,1,3,2]))
print(longestConsecutinve([0,3,7,2,5,8,4,6,0,1]))