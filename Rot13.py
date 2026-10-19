import string
def rot13(message):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    message = list(message)
    for i in range(len(message)):
        position = None
        if message[i] in uppercase:
            position = uppercase.index(message[i]) % 26
            message[i] = uppercase[(position+13)%26]
        elif message[i] in lowercase:
            position = lowercase.index(message[i])
            message[i] = lowercase[(position+13)%26]
        else:
            continue
    return ''.join(message)
while True:
    message = input('Transform To Rot13: ')
    if message in ['exit', 'e']:
        exit()
    print(rot13(message))
