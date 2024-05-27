# Function to perform quick sort on an array
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

# Function to partition the array around a pivot element
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Function to replace all occurrences of a target element with a replacement element
def replace_element(arr, target, replacement):
    for i in range(len(arr)):
        if arr[i] == target:
            arr[i] = replacement

# Prompt the user to input an array of integers
arr = list(map(int, input("Enter an array of integers: ").split()))

# Perform quick sort on the input array
quick_sort(arr, 0, len(arr) - 1)

# Allow the user to specify a target element to search for in the sorted array
target = int(input("Enter a target element to search for: "))

# If the target element is found, prompt the user to input a replacement element
if target in arr:
    replacement = int(input("Enter a replacement element: "))
    replace_element(arr, target, replacement)

# Display the modified array after replacing the elements
print("Modified array:", arr)