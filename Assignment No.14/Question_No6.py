#### Q.6 : Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.

def max_product(nums):
    nums = list(set(nums))   # using set
    max_product = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            product = nums[i] * nums[j]

            if product > max_product:
                max_product = product
                pair = (nums[i], nums[j])

    print("Numbers:", pair)
    print("Maximum Product:", max_product)

numbers = [1, 5, 2, 9, 7, 9]

max_product(numbers)