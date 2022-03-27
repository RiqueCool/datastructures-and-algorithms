
def insertion_sort(old_arr):
    arr = list(old_arr)

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] =  arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr

def test():
    input = [9, 5, 1, 4, 3]
    expected = [1, 3, 4, 5, 9]
    result = insertion_sort(input)

    assert result == expected, '\n\n\tExpected: {} \n\tResult: {}\n'.format(expected, result)

test()
