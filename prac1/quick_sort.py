from time import time 
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

sequence = [78, 12, 15, 45, 34]
print(f"Unsorted: {sequence}")
start_time = time()
sorted = quick_sort(sequence)
end_time = time()
print(f"Sorted: {sorted}")
total_time = end_time - start_time
print(f"Time taken for execution: {total_time}")

# Example:

# Given sequence = [78, 12, 15, 45, 34], the pivot is chosen as 34.
# items_greater would contain [78, 45] (elements greater than 34).
# items_lower would contain [12, 15] (elements less than or equal to 34).
# After recursively sorting [12, 15] and [78, 45], and concatenating them with 34 in between, the final sorted sequence would be
#  [12, 15, 34, 45, 78].