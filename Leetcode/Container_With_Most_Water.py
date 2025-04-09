# 作者：Alex
# 2025/4/5 11:50
def container_with_most_water(height):
    max_water = 0
    # for i in range(len(height) - 1):
    #     for j in range(1,len(height)):
    #         if i + j > len(height) - 1:
    #             break
    #         max_water = max(max_water, min(height[i], height[i + j]) * j)
    # return max_water

    left, right = 0, len(height) - 1
    while left < right:
        high = min(height[left], height[right])
        width = right-left
        max_water = max(max_water, high * width)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_water


print(container_with_most_water([1,8,6,2,5,4,8,3,7]))