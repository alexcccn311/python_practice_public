# 作者：Alex
# 2024/10/17 06:05
from statistics import median
from typing import List


"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1+ nums2)
        l = len(nums3)
        if l%2 == 0:
            median = (nums3[int((l-1)/2)]+nums3[int((l+1)/2)])/2
        else:
            median = nums3[int(l/2)]
        return median
"""

"""
###二分查找标准函数
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # 找到目标值，返回索引
        elif arr[mid] < target:
            left = mid + 1  # 缩小左侧范围
        else:
            right = mid - 1  # 缩小右侧范围

    return -1  # 没找到目标值
"""

class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            max_left_1 = nums1[i - 1] if i > 0 else float('-inf')
            min_right_1 = nums1[i] if i < m else float('inf') #lower_half_nums1,nums1[i - 1],nums1[i],higher_half_nums_1

            max_left_2 = nums2[j - 1] if j > 0 else float('-inf')
            min_right_2 = nums2[j] if j < n else float('inf') #lower_of_nums2 ((m + n + 1) // 2 - i - 2),nums2[(m + n + 1) // 2 - i - 1], nums2[(m + n + 1) // 2 - i], higher_of_nums2 (n/2 - m/2 + i)

            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                if (m + n) % 2 == 0:
                    return (max(max_left_1, max_left_2) + min(min_right_1, min_right_2)) / 2
                else:
                    return max(max_left_1, max_left_2)
            elif max_left_1 > min_right_2:
                right = i - 1
            else:
                left = i + 1


"""class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        a, b = 0, 0
        while True:
            median_nums1 = nums1[m//2 * a]
            median_nums2 = nums2[n//2 * b]
            if median_nums1 < median_nums2: #去除nums1的前半段和nums2的后半段
                a *= 1.5
                b = b *2/3
            elif median_nums1 > median_nums2:
                a = a * 2/3
                b *= 1.5
            else:
                return (median_nums1 + median_nums2) / 2"""



"""nums1 = [5, 6, 7]
nums2 = [1, 2, 3, 4]
print(Solution.findMedianSortedArrays(nums1, nums2))"""

"""
#最后利用float('inf')解决边界问题就和标准答案一样了
class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        i = m//2
        j = (m + n + 1) // 2 - i

        while True:
            if j == n- 1:
                if (m + n) % 2 == 0:
                    pass
                else:
                    pass
            if nums2[j] <= nums1[i] <= nums2[j + 1]:
                if (m + n) % 2 == 0:
                    return (nums1[i] + max(nums1[i-1],nums2[j]))/2
                else:
                    return nums1[i]
            elif nums1[i] >= nums2[j + 1]:
                i -= 1
            elif nums1[i] <= nums2[j]:
                i += 1
            if i == m:
                if (m + n) % 2 == 0:
                    return (nums1[i]+nums2[j])/2
                else:
                    return nums2[j]"""

