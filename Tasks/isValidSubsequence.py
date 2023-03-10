#   Given two non-empty arrays of integers, write a function that determines
#   whether the second array is a subsequence of the first one.
#
#   A subsequence of an array is a set of numbers that aren't necessarily adjacent
#   in the array but that are in the same order as they appear in the array. For
#   instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4],
#   and so do the numbers [2, 4]. Note that a single number in an array is also a
#   valid subsequence of the array.
#
#   Sample Input:
#   array = [5, 1, 22, 25, 6, -1, 8, 10]
#   sequence = [1, 6, -1, 10]
#
#   Sample Output:
#   True


def subsequenceCheck (array, sequence):
    arrayIdx = 0
    seqIdx = 0
    while arrayx < len(array) and seqx < len(sequence):
        if array[arrayIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrayIdx += 1
    if seqIdx == len(sequence):
        return True
    else:
        return False
