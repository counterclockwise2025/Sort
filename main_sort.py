'''
Samip Vaidh
Sorting
4/14/20
'''

import random

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
def middle_pivot(nums, low, high):
    i=(low-1)
    pivot_point=nums[high]

    for j in range (low, high):
        if nums[j] <= pivot_point:
            i=i+1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[high] = nums[high], nums[i+1]
    return(i+1)

#heap sort algo
def heap_sort(nums, n, i):
    biggest = i
    l = 2 * i+1
    r = 2 * i+2

    if l < n and nums[i] < nums[l]:
        biggest = 1

    if r < n and nums[biggest] < nums[r]:
        biggest = r

    if biggest != i:
        nums[i], nums[biggest] = nums[biggest], nums[i]
        heap_sort(nums, n, biggest)

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
