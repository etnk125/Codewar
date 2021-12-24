def rot13(message):
    ans = ""
    for i in message:
        ans += chr(ord(i)+cal(i))
    return ans


def cal(c):
    if 'a' <= c.lower() <= 'm':
        return 13
    elif 'n' <= c.lower() <= 'z':
        return -13
    else:
        return 0


    """
    import string
    from codecs import encode as _dont_use_this_
    from string import maketrans, lowercase, uppercase

    def rot13(message):
        lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
        upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
        return message.translate(lower).translate(upper)
    """