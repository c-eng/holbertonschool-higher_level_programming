def uppercase(str):
    temp = ''
    for ind in range(len(str)):
        if ord(str[ind]) >= 97 and ord(str[ind]) <= 122:
            temp += chr(ord(str[ind]) - 32)
        else:
            temp += chr(ord(str[ind]))
    print(temp)
