'''
Samip Vaidh
Sorting
4/14/20
'''

import random
import time
import pdb
import matplotlib.pyplot as plt

#random number geneator between 1 to 20000 without dups
def randNumGen(n):
    nums = set()
    while len(nums) < n:
        nums.add(random.randint(1, 20000))
    return list(nums)

#insertion sort algo
def insert_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j=i-1
        while j>=0 and key < nums[i]:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key

#quick sort algo
def middle(nums, l, h):
    i = (l - 1)
    x = nums[h]

    for j in range(l, h):
        if nums[j] <= x:
            i = i+1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[h] = nums[h], nums[i+1]
    return (i+1)

def quick_sort_algo(nums, l, h):

    size = h - l + 1
    stack = [0] * (size)

    top = -1

    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:


        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        p = middle(nums, l, h)

        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

def quick_sort(nums):
    quick_sort_algo(nums, 0, len(nums)-1)

#heap sort algo
def heap_algo(nums, n, i):
    biggest = i
    l = 2 * i + 1 
    r = 2 * i + 2     

    if l < n and nums[i] < nums[l]:
        biggest = l

    if r < n and nums[biggest] < nums[r]:
        biggest = r

    if biggest != i:
        nums[i], nums[biggest] = nums[biggest], nums[i]

        heap_algo(nums, n, biggest)

def heap_sort(nums):
    n = len(nums)

    for i in range(int(n/2) - 1, -1, -1):
        heap_algo(nums, n, i)

    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i] 
        heap_algo(nums, i, 0)

#merge sort algo
def merge_sort(nums):
    if len(nums) > 1:
        middle = len(nums)//2
        left = nums[:middle]
        right = nums[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            nums[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            nums[k] = right[j]
            j+=1
            k+=1

def test_complexity(sorting_algo, algo_name):
    size_of_list = [100, 500, 1000, 2000, 5000, 8000, 10000]
    #create a time stamp numsay/list
    time_stamp = []
    for n in size_of_list:
        gen_nums = randNumGen(n)
        #get the initial time
        time_initial = time.time()
        sorting_algo(gen_nums)
        time_final = time.time()
        print("Time ellapsed using {} n = {}: {}".format(algo_name, n, time_final - time_initial))
        time_stamp.append(time_final-time_initial)
    return time_stamp


def test_complexity_sorted(sorting_algo, algo_name):
    size_of_list = [100, 500, 1000, 2000, 5000, 8000, 10000]
    #create a time stamp numsay/list
    time_stamp = []
    for n in size_of_list:
        gen_nums = randNumGen(n)
        gen_nums.sort()
        #get the initial time
        time_initial = time.time()
        sorting_algo(gen_nums)
        time_final = time.time()
        print("Time ellapsed using {} n = {}: {}".format(
            algo_name, n, time_final - time_initial))
        time_stamp.append(time_final-time_initial)
    return time_stamp

time_complexity_insertion_unsort = test_complexity(insert_sort, "Insertion Sort")
time_complexity_quick_unsort = test_complexity(quick_sort, "Quick Sort")
time_complexity_heap_unsort = test_complexity(heap_sort, "Heap Sort")
time_complexity_merge_unsort = test_complexity(merge_sort, "Merge Sort")

time_complexity_insertion_sorted = test_complexity_sorted(insert_sort, "Insertion Sort")
time_complexity_quick_sorted = test_complexity_sorted(quick_sort, "Quick Sort")
time_complexity_heap_sorted = test_complexity_sorted(heap_sort, "Heap Sort")
time_complexity_merge_sorted = test_complexity_sorted(merge_sort, "Merge Sort")

#creating the graphs for each of the complexitiey
x = [100, 500, 1000, 2000, 5000, 8000, 10000]
plt.plot(x, time_complexity_insertion_unsort, label = 'Insertion Sort')
plt.plot(x, time_complexity_quick_unsort, label = 'Quick Sort')
plt.plot(x, time_complexity_heap_unsort, label = 'Heap Sort')
plt.plot(x, time_complexity_merge_unsort, label = "Merge Sort")
plt.yscale("log")

plt.title("Unsorted Complexity")
plt.xlabel('n')
plt.ylabel('Time')

plt.legend()
plt.savefig("Unsorted Complexity.png")

#creating the graphs for each of the complexitiey
x = [100, 500, 1000, 2000, 5000, 8000, 10000]
plt.plot(x, time_complexity_insertion_sorted, label='Insertion Sort')
plt.plot(x, time_complexity_quick_sorted, label='Quick Sort')
plt.plot(x, time_complexity_heap_sorted, label='Heap Sort')
plt.plot(x, time_complexity_merge_sorted, label="Merge Sort")
plt.yscale("log")

plt.title("Sorted Complexity")
plt.xlabel('n')
plt.ylabel('Time')

plt.legend()
plt.savefig("Sorted Complexity.png")
