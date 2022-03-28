
def bubble_sort(old_arr):
    arr = list(old_arr)
    
    for j in range(len(arr)):
        swapped = False

        for i in range(len(arr) - j - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
                swapped = True

        if not swapped:
            break

    return arr

def test():
    input = [9, 5, 1, 4, 3]
    expected = [1, 3, 4, 5, 9]
    result = bubble_sort(input)

    assert result == expected, '\n\n\tExpected: {} \n\tResult: {}\n'.format(expected, result)

test()
