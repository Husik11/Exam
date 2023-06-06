height = [4, 2, 0, 3, 2, 5]

def trap(height):
    if not height:
        return 0
    water = 0
    n = len(height)
    for i in range(1, n - 1):
        left_max = max(height[:i])
        right_max = max(height[i + 1:])
        min_height = min(left_max, right_max)
        if min_height > height[i]:
            water += min_height - height[i]
    return water
print(trap(height))

