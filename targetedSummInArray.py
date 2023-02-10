# Find a pair of numbers in array which summ equal targetSum
# Solution 1
# Sample input:
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10


def summarize(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return[]

# Solution 2
def summarize2(array, targetSum):
    nums = {}
    for num in array:
        Match = targetSum - num
        if Match in nums:
            return [Match, num]
        else:
            nums[num] = True
    return []
