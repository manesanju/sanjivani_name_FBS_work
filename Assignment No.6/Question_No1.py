##### Q : Write a program print following patterns:

# a)   * * * * *
    #  *       *
    #  *       *
    #  *       *
    #  * * * * *

for i in range(1,6):
    for j in range(1,6):
        if(i == 1 or i == 5 or j == 1 or j ==5):
            print('*',end =' ')
        else:
            print(' ',end =' ')
    print()

# b)   1
    #  2 3
    #  4 5 6
    #  7 8 9 10

num = 1
for i in range(1, 5):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()
  
# c)            1
        #      1  1
        #     1  2  1
        #    1  3  3  1

for i in range(1, 5):

    for j in range(1, 5 - i):
        print(" ", end=" ")

    val = 1
    for j in range(1, i + 1):
        print(val, end="   ")
        val = val * (i - j) // j

    print()

# d)   A
    #  A B
    #  A B C 
    #  A B C D
    #  A B C D E

for i in range(1, 6):
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()

# e)      * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        print('*',end=' ')
    for j in range(1,i):
        print('*',end=' ')
    print()

# f)      1 
#       1 2 3 
#     1 2 3 4 5 
#   1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 8 9 

for i in range(1, 6):

    for j in range(1, 6 - i):
        print(" ", end=" ")

    for j in range(1, 2 * i):
        print(j, end=" ")

    print()

# g)      A 
#       A B C 
#     A B C D E 
#   A B C D E F G 
# A B C D E F G H I

for i in range(1, 6):

    for j in range(1, 6 - i):
        print(" ", end=" ")

    for j in range(1, 2 * i):
        print(chr(64 + j), end=" ")

    print()