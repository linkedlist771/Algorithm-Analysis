class MergeSort:
    """
    Implementation of the merge sort algorithm.
    """

    @staticmethod
    def merge(array: list[int], start: int, mid: int, end: int) -> list[int]:
        """
        Merge two sorted sub-arrays into one.

        Parameters:
        - array: The array containing the two sub-arrays.
        - start: The starting index of the first sub-array.
        - mid: The ending index of the first sub-array.
        - end: The ending index of the second sub-array.

        Returns:
        - The merged array.
        """
        left_length = mid - start + 1
        right_length = end - mid
        left_subarray = [None] * (left_length + 1)
        right_subarray = [None] * (right_length + 1)

        for i in range(left_length):
            left_subarray[i] = array[start + i]
        for i in range(right_length):
            right_subarray[i] = array[mid + i + 1]

        # Sentinel values
        left_subarray[left_length] = float('inf')
        right_subarray[right_length] = float('inf')

        i, j = 0, 0
        for k in range(start, end + 1):
            if left_subarray[i] <= right_subarray[j]:
                array[k] = left_subarray[i]
                i += 1
            else:
                array[k] = right_subarray[j]
                j += 1

        return array

    def sort(self, array: list[int], start_pos: int = 0, end_pos: int = None) -> list[int]:
        """
        Sort the array using the merge sort algorithm.

        Parameters:
        - array: The array to be sorted.
        - start_pos: The starting index of the array segment to be sorted (default is 0).
        - end_pos: The ending index of the array segment to be sorted (default is the last element).

        Returns:
        - The sorted array.
        """
        if end_pos is None:
            end_pos = len(array) - 1

        if start_pos < end_pos:
            mid_pos = (start_pos + end_pos) // 2  # Integer division
            self.sort(array, start_pos, mid_pos)
            self.sort(array, mid_pos + 1, end_pos)
            self.merge(array, start_pos, mid_pos, end_pos)

        return array


if __name__ == "__main__":
    test_array = [2, 1, 45, 21, 5]
    sorter = MergeSort()
    sorted_result = sorter.sort(test_array)
    print(sorted_result)
