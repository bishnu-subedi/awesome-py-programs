# Binary Search

def binary_search(start, end, int_list, target):
    # Check if element is not present
    if start <= end:
        mid = (start + end) // 2

        # Check if middle element is the target element
        if int_list[mid] == target:
            return mid + 1

        # If not, check if lesser than middle element
        # Change range to start to mid-1, since less than mid
        elif target < int_list[mid]:
            return binary_search(start, mid - 1, int_list, target)

        # Check if greater than middle element
        # Change range to mid+1 to end, since greater than mid
        elif target > int_list[mid]:
            return binary_search(mid + 1, end, int_list, target)

    else:
        return -1


# Read length of list
length = int(input("Enter length of list: "))
int_list = []

# Read elements of list
for i in range(length):
    element = int(input("Enter element: "))
    int_list.append(element)

# Sort the list
int_list = sorted(int_list)
print(int_list)

# Read target element to be found
target = int(input("Enter target element: "))

position = binary_search(0, length - 1, int_list, target)

if position == -1:
    print('Element not in list')
else:
    print("Element found at position: " + str(position))
