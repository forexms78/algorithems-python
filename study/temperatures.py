def dailtTemperatures(temperatures):
    ans = [0] * len(temperatures)
    stack = []
    # enumerate는 index를 추적할때 좋다
    for cur_day, cur_temp in enumerate(temperatures):
        # stack[-1][1]이 의미하는것은 [-1]은 최상단을 가르치고 [1]은 [0]은 prev_day [1]은 cur_temp를 가르킨다
        while stack and stack[-1][1] < cur_temp:
            prev_day, _ = stack.pop()
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))
    return ans
dailtTemperatures([73,74,75,71,69,72,76,73])