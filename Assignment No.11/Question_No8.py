#### Q.8 : Print 1 to 100 in snakes and ladder pattern.

def snake_ladder():

    num = 1

    for i in range(10):

        if i % 2 == 0:

            for j in range(10):
                print(num, end="\t")
                num = num + 1

        else:

            temp = num + 9

            for j in range(10):
                print(temp, end="\t")
                temp = temp - 1

            num = num + 10

        print()

snake_ladder()