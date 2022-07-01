#PROGRAM TO FIND THE AVERAGE OF K NUMBER OF ELEMENTS

#BRUT FORCE
#Time Complexity: O(n*k)
from numpy import result_type


nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
"""
result = []
windowSum = 0

for i in range(len(nums)-k+1):
    windowSum = 0

    for j in range(i, i+k):
        windowSum += nums[j]
    result.append(windowSum/k)

print (result)
"""

#OPTIMIZED
result = []
windowStart = 0
windowSum = 0

for windowEnd in range(len(nums)):
    windowSum += nums[windowEnd]

    if windowEnd >= k - 1:
        result.append(windowSum/k)
        windowSum -= nums[windowStart]
        windowStart += 1

print (result)
