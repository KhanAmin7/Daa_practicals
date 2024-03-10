from time import time

def insertion_sort(list1):
    for i in range(1, len(list1)):
        j = i
        while list1[j - 1] > list1[j] and j > 0:
            list1[j - 1], list1[j] = list1[j], list1[j - 1]
            j-=1

list1 = [6, 4, 1, 3, 9, 8]
print(f"Unsorted list: {list1}")

total_time = 0
num_iter = 1000
for k in range(num_iter):
    start_time = time()
    insertion_sort(list1)
    end_time = time()
    total_time += end_time - start_time
    avg_time = total_time/num_iter 

print(f"Sorted: {list1}")
print(f"Average execution time: {avg_time}")
