from time import time

def bubble_sort(list1):#https://www.youtube.com/watch?v=g_xesqdQqvA
    indexing_length = len(list1) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list1[i] > list1[i + 1]:  # Compare adjacent elements for sorting
                sorted = False
                list1[i], list1[i + 1] = list1[i + 1], list1[i]

# Function to measure the time taken for bubble sort

# Example usage
list1 = [5, 2, 80, 45, 1]
print("Unsorted:", list1)

total_time = 0
num_iteration = 1000

for k in range(num_iteration):
    start_time = time()
    bubble_sort(list1)
    end_time = time()
    total_time+= end_time - start_time

avg_time = total_time/num_iteration
print(f"sorted list {list1}")
print(f"Average execution time taken: {avg_time}")
