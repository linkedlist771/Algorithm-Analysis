class QuickSort:
    """
    Implementation of the quicksort algorithm.
    """

    @staticmethod
    def partition(array: list[int], start: int, end: int) -> int:
        """
        Partition the array segment into two sub-segments.

        Parameters:001.
        - array: The array segment to be partitioned.
        - start: The starting index of the array segment.
        - end: The ending index of the array segment.

        Returns:
        - The index of the pivot after partitioning.
        """
        pivot = array[end]
        i = start - 1
        for j in range(start, end):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[end] = array[end], array[i + 1]
        return i + 1

    def sort(self, array: list[int], start_pos: int = 0, end_pos: int = None) -> list[int]:
        """
        Sort the array using the quicksort algorithm.

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
            pivot_pos = self.partition(array, start_pos, end_pos)
            self.sort(array, start_pos, pivot_pos - 1)
            self.sort(array, pivot_pos + 1, end_pos)

        return array


if __name__ == "__main__":
    test_array = [2, 1, 45, 21, 5]
    sorter = QuickSort()
    sorted_result = sorter.sort(test_array)
    print(sorted_result)
