# Find the numbers from the given sequence, which contains in array in the same order
# Sample input:
# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [-1, 1, 3, -1, 12, 10]
# Sample output:
# [1, -1, 10]


def sequenceCheck(array, sequence):
    result = []
    result = [s for s in array if s in sequence]
    return result
