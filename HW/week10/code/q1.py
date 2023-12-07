def find_max_subarray(array):
    def find_max_sub(array, left, right):
        # Base case: single element
        if left == right:
            return array[left]
        mid = (left + right) // 2
        left_max_sum = find_max_sub(array, left, mid)
        right_max_sum = find_max_sub(array, mid+1, right)
        cross_sum_max = find_cross_sum_max(array, left, right, mid)
        return max(left_max_sum, right_max_sum, cross_sum_max)

    def find_cross_sum_max(array, left, right, mide):
        if left == right:
            return array[left]
        left_sum_max = -float('inf')
        right_sum_max = -float('inf')
        left_sum = 0
        right_sum = 0
        for i in range(mide, left-1, -1):
            left_sum += array[i]
            if left_sum > left_sum_max:
                left_sum_max = left_sum
        for j in range(mide+1, right+1):
            right_sum += array[j]
            if right_sum > right_sum_max:
                right_sum_max = right_sum
        return left_sum_max + right_sum_max

    return find_max_sub(array, 0, len(array)-1)


def find_max_subarray_by_dp(array):
    max_sum = - float('inf')
    sum = 0
    size = len(array)
    for i in range(size):
        sum += array[i]
        if sum > max_sum:
            max_sum = sum
        if sum < 0:
            sum = 0
    return max_sum



# give an instance to test
if __name__ == "__main__":
    test_array = [2, 1, 45, 21, 5]
    print(find_max_subarray(test_array))
    print(find_max_subarray_by_dp(test_array))