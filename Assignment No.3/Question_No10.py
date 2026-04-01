##### Q.10 : Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

# Take input
gender = input('Enter gender(M/F):')
age = int(input('Enter age:'))

# check eligibility
if(gender in ['F','f','FEMALE','Female','female']):                 
    if(age >= 18):
        print('Eligible for marriage')
    else:
        print('Not Eligible for marriage')
if(gender in ['M','m','MALE','Male','male']):
    if(age >= 21):
        print('Eligible for marriage')
    else:
        print('Not eligible for marriage')