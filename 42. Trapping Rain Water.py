height = [4, 2, 0, 3, 2, 5]

# def trap(height):
#     if not height:
#         return 0
#     w_trap = 0
#     n = len(height)
#     for i in range(1, n - 1):
#         left_max = max(height[:i])
#         right_max = max(height[i + 1:])
#         min_height = min(left_max, right_max)
#         if min_height > height[i]:
#             w_trap += min_height - height[i]
#     return w_trap
# print(trap(height))

def trap(height):
    if not height:
        return 0
    l = 0
    r = len(height) - 1
    leftMax = height[l]
    rightMax = height[r]
    sum = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            sum += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            sum += rightMax - height[r]
    return sum
print(trap(height))



