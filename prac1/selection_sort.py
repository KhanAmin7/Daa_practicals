from time import time 

def selection_sort(list1):
    for i in range(len(list1)):
        min_val = min(list1[i:])
        min_val_ka_index = list1.index(min_val)
        list1[i], list1[min_val_ka_index] = list1[min_val_ka_index], list1[i]

list1 = [15, 45, 12, 32, 4]
print(f"Unsorted {list1}")
start_time = time()
sorted = selection_sort(list1)
end_time = time()
ext_time = end_time - start_time   
print(f"Sorted {list1}")
print(f"Average execution time taken: {ext_time}")