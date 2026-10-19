import re
print('This can check only 1 ipv4 address.')
print("Only Input the ip address only, if you don't it will return False.")
strng = input('Check IP adderss: ')
def is_valid_IP(strng):
    ip_regex = re.compile(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})')
    mo = ip_regex.fullmatch(strng)
    if not mo:
        return False
    for i in mo.groups():
        if i.startswith('0') and len(i) > 1:
            return False
        try:
            if int(i) >= 0 and int(i) <= 255:
                pass
            else:
                return False
        except ValueError:
            return False
    return True
print(is_valid_IP(strng))
