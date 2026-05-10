##### Q : Write a program print following patterns:

# a)                       *
                    #     * *
                    #    *   *
                    #   *     *
                    #  *       *
                    #  *       *
                    #   *     *
                    #    *   *
                    #     * *
                    #      *

# Upper part
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower part
for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# b) * 
   # * * 
   # * * * 
   # * * * * 
   # * * * * * 
   # * * * * 
   # * * * 
   # * * 
   # * 

for i in range(1,6):
    for j in range(1, i+1):
        print('*',end=' ')
    print()

for i in range(1, 5):
    for j in range(1, 6-i):
        print('*',end=' ')
    print()

# c)   1
    #  1 2
    #  1   3
    #  1     4
    #  1 2 3 4 5   
     
for i in range(1, 6):
    for j in range(1, i + 1):
        if i == 5 or j == 1 or j == i:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

# d)                      1
                #       2 3 2
                #     3 4 5 4 3
                #   4 5 6 7 6 5 4
                # 5 6 7 8 9 8 7 6 5

for i in range(1, 6):
    
    # spaces
    for j in range(5 - i):
        print(" ", end=" ")
    
    # increasing numbers
    for j in range(i, 2*i):
        print(j, end=" ")
    
    # decreasing numbers
    for j in range(2*i - 2, i - 1, -1):
        print(j, end=" ")
    
    print()


# e)               1
            #     1 2
            #    1   3
            #   1     4
            #  1 2 3 4 5   

for i in range(1, 6):
    
    # center spaces
    for j in range(6 - i):
        print(" ", end="")
    
    # numbers
    for j in range(1, i + 1):
        if i == 5 or j == 1 or j == i:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    
    print()

# f)   1 2 3 4 5
    #  2     5
    #  3   5
    #  4 5
    #  5

for i in range(1, 6):
    
    for j in range(i, 6):
        if i == 1 or j == i or j == 5:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    
    print()

# g)                    1
            #         1 2 1
            #       1 2 3 2 1
            #     1 2 3 4 3 2 1
            #   1 2 3 4 5 4 3 2 1

for i in range(1, 6):
    
    # spaces
    for j in range(5 - i):
        print(" ", end=" ")
    
    # increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    
    print()

# h)1                 1
#   1 2             2 1
#   1 2 3         3 2 1
#   1 2 3 4     4 3 2 1
#   1 2 3 4 5 5 4 3 2 1              

rows = 5

for i in range(1, rows + 1):

    # Left side numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # Middle spaces
    spaces = (rows - i) * 4
    print(" " * spaces, end="")

    # Right side numbers
    for j in range(i, 0, -1):
        print(j, end=" ")

    print()

       