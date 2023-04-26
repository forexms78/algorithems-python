def longestConsecutinve(nums):
    num_dict = {}
    longest = 0

    for num in nums:
        num_dict[num] = True
    
    for num in num_dict:
        if num - 1 not in num_dict:
            cnt = 1
            target = num + 1
            while target in num_dict:
                target += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest
            

print(longestConsecutinve([100,4,200,1,3,2]))
print(longestConsecutinve([0,3,7,2,5,8,4,6,0,1]))