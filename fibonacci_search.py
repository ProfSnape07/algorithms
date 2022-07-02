def fib_search(array, search_int):
    n = len(array)
    fib_0 = 0
    fib_1 = 1
    fib_2 = fib_1 + fib_0
    offset = -1

    while fib_2 < n:
        fib_0 = fib_1
        fib_1 = fib_2
        fib_2 = fib_1 + fib_0

    while fib_2 > 1:
        # when sub-array is of length 1 then fib_2 will be 1.
        # also loop starts only when array is of length more than 1.
        index = min((offset + fib_0), n - 1)

        if array[index] < search_int:
            fib_2 = fib_1
            fib_1 = fib_0
            fib_0 = fib_2 - fib_1

            offset = index

        elif array[index] > search_int:
            for a in range(2):
                fib_2 = fib_1
                fib_1 = fib_0
                fib_0 = fib_2 - fib_1

        else:
            # element found, returning required index.
            return index

    if array[n - 1] == search_int:
        # checking last element and only element if the given array is of length 1.
        index = n - 1
        return index

    else:
        # returning None if element not found.
        return


user_input = input("Enter the elements of the array separated by comma: ")
array_0 = sorted(int(item) for item in user_input.split(","))
search_int_0 = int(input("Enter a number to search in the array: "))
# array_0 = [0, 90, 21, 4343, 434, 432, 54, 413, 3, 34, 23, 32, 422, 98]
# array_0.sort()
# search_int_0 = 43
print(f"Sorted array: {array_0}")
print("Initializing Fibonacci Search.")
calling_search_function = fib_search(array_0, search_int_0)

if calling_search_function is not None:
    print(f"\"{search_int_0}\" is found at the index {calling_search_function} of the array.")
else:
    print(f"\"{search_int_0}\" isn`t present in the array.")
