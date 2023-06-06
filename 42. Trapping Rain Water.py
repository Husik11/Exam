height = [4, 2, 0, 3, 2, 5]

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



