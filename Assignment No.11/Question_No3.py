#### Q.3 : Python Program to Sort the List According to the Second Element in Sublist.

def sort_list(data):

    for i in range(len(data)):
        for j in range(i + 1, len(data)):

            if data[i][1] > data[j][1]:

                temp = data[i]
                data[i] = data[j]
                data[j] = temp

    print(f'Sorted List is {data}.')

data = [[1, 5], [2, 3], [4, 1], [3, 2]]

sort_list(data)