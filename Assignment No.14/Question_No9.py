#### Q.9 : Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

def find_combinations(nums, target):
    result = set()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    result.add((nums[i], nums[j], nums[k]))

    print("Combinations are:")
    for combo in result:
        print(combo)

numbers = [1, 2, 3, 4, 5, 6]
target = 10

find_combinations(numbers, target)