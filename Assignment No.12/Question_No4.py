#### Q.4 : Python Program to Form a New String where the First Character and the Last Character have been Exchanged

def exchange_characters(text):
    if len(text) <= 1:
        return text
    new_text = text[-1] + text[1:-1] + text[0]
    return new_text

string = input("Enter a string: ")
result = exchange_characters(string)
print("New string:", result)