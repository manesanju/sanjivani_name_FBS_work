#### Q.2 : Python Program to Merge Two Lists and Sort it.

def merge_sort(list1, list2):

    merged_list = list1 + list2

    for i in range(len(merged_list)):
        for j in range(i + 1, len(merged_list)):

            if merged_list[i] > merged_list[j]:

                temp = merged_list[i]
                merged_list[i] = merged_list[j]
                merged_list[j] = temp

    print(f'Merged and Sorted List is {merged_list}.')

list1 = [30, 10, 50]
list2 = [20, 40, 15]

merge_sort(list1, list2)