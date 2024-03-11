def binary_find(array, element, left, right):
    if left > right:
            return False
    middle = (right + left) // 2
    if element == array[middle]:
        if array[middle - 1] < element and element <= array[middle]:
            return middle
        elif element < array[middle]:
            return binary_find(array, element, left, middle - 1)
    elif element == array[middle - 1]:
            return binary_find(array, element, left, middle - 1)
    else:
            return binary_find(array, element, middle + 1, right)
array = list(map(int, input("Enter integers in any order, separated by spaces: ").split()))
element = int(input("Enter any positive integer from the entered list: "))
array = sorted(array)
print(array)
left = int(array[0])
right = int(array[-1])
if element < left or element > right:
    print("Number not in range")
else:
    print(binary_find(array, element, 0, len(array) - 1))