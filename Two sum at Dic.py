def two_sum(nums, target):
    memo = {}
    for v in nums:
        memo[v] = 1

    for v in nums:
        needed_number = target - v
        if v == needed_number:
            return False
        if needed_number in memo:
            return True

    return False

print(two_sum({1,2,4,7,9,11,16},14))
    