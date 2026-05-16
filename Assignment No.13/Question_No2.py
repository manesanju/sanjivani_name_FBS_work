#### Q.2 : Python Program to Concatenate Two Dictionaries Into One

dict1 = {
    "a": 10,
    "b": 20
}
dict2 = {
    "c": 30,
    "d": 40
}
dict3 = {}
for key in dict1:
    dict3[key] = dict1[key]
for key in dict2:
    dict3[key] = dict2[key]
print("Concatenated Dictionary:", dict3)