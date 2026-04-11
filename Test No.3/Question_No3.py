# Q.3: Write a program to accept basic salary of n emp. (n should be
# accepted from user). If basic salary is below 20000 then
# da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and
# hra=20%. Based on this calculate the total salary of each emp
# and also total salary of all emp.

n = int(input('Enter number of employees: '))

total_all = 0

for i in range(n):
    print('\nEmployee', i + 1)
    basic = float(input('Enter basic salary: '))

    if basic < 20000:
        da = 0.10 * basic
        ta = 0.12 * basic
        hra = 0.15 * basic
    else:
        da = 0.15 * basic
        ta = 0.18 * basic
        hra = 0.20 * basic

    total = basic + da + ta + hra
    print(f'Total salary is {total}.')

    total_all += total

print(f'Total salary of {n} employees is {total_all}.')