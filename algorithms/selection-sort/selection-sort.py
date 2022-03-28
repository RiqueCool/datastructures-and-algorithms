
def selection_sort(old_arr):
    arr = list(old_arr)
    size = len(arr)

    for i in range(size):
        m = i

        for j in range(i + 1, size):
            if arr[j] < arr[m]:
                m = j

        (arr[m], arr[i]) = (arr[i], arr[m])

    return arr

def test():
    input = [9, 5, 1, 4, 3]
    expected = [1, 3, 4, 5, 9]
    result = selection_sort(input)

    assert result == expected, '\n\n\tExpected: {} \n\tResult: {}\n'.format(expected, result)

test()
