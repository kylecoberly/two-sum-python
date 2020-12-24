def two_sum(number_list, target_number):
    permutations = get_permutations(number_list)

    for permutation in permutations:
        first_number = number_list[permutation[0]]
        second_number = number_list[permutation[1]]

        if first_number + second_number == target_number:
            return permutation

def get_permutations(number_list):
    length = len(number_list)
    result = []

    for pivotIndex in range(length):
        for stretchIndex in range(pivotIndex + 1, length):
            result.append((pivotIndex, stretchIndex))

    return result

print two_sum([4, 0], 4), "This should be (0, 1)"
print two_sum([4, 0, 0], 4), "This should be (0, 1) or (0, 2)"
print two_sum([1, 1, 1], 2), "This should be (0, 1) or (0, 2) or (1, 2)"
print two_sum([1, 2, 3], 4), "This should be (0, 2)"
print two_sum([1, 5, 27, 0, 0, 20, 15, 73], 100), "This should be (2, 7)"
