# Finding a pair of numbers in array which summ equal targetSum
# Solution 1
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10
#
# def summarize(array, targetSum):
#     for i in range(len(array) - 1):
#         firstNum = array[i]
#         for j in range(i + 1, len(array)):
#             secondNum = array[j]
#             if firstNum + secondNum == targetSum:
#                 print(firstNum, secondNum)
#                 return [firstNum, secondNum]
#     return[]
#
# Solution 2
# def summarize2(array, targetSum):
#     nums = {}
#     for num in array:
#         Match = targetSum - num
#         if Match in nums:
#             print(Match, num)
#             return [Match, num]
#         else:
#             nums[num] = True
#     return []
#
# summarize(array, targetSum)
# summarize2(array, targetSum)
#
# Finding a subsiquense
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [-1, 1, 3, -1, 12, 10]

def isValidSubsequence(array, sequence):
    result = []
    result = [s for s in array if s in sequence]
    print(result)
    return print ("True")
isValidSubsequence(array, sequence)

# Failed versions
# def summarize():
#     start_num = 0
#     end_num = len(array)-1
#     result_list = []
#     for i in range(start_num, end_num):
#         first_num = 0
#         second_num = first_num + 1
#         if first_num+second_num == targetSum:
#             result = first_num+second_num
#             result_list.append(result)
#         elif first_num == end_num:
#             start_num +=1
#         first_num +=1
#     print(result_list)
#
#
#     # done = False
#     # while not done:
#     #     start_num = 0
#     #     end_num = len(array) - 1
#     #     for i in range(start_num, end_num):
#     #         result_list = []
#     #         first_num = i
#     #         second_num = first_num + 1
#     #         # while first_num != end_num:
#     #         if first_num + second_num == targetSum:
#     #             result = first_num + second_num
#     #             result_list.append(result)
#     #         elif start_num == end_num:
#     #             return result_list
#     #             done = True
#     # print(result_list)
#
# summarize()