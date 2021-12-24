def find_missing_letter(chars):
    for prev, curr in zip(chars, chars[1:]):
        print(prev, curr)
        if ord(curr) != ord(prev)+1:
            return chr(ord(prev)+1)
"""
def find_missing_letter(c):
    return next(chr(ord(e)+1) for i, e in enumerate(c) if ord(e)+1 != ord(c[i+1]))
    

    use emunerate to get index and element in for

    next() gets the first value that satisfies the generator expression. next(item for item in [0,1] if item == 1) is like [item for item in [0,1] if item == 1][0] but next() stops at the first hit and doesn't traverse the whole iterable, so is more efficient. see: https://docs.python.org/3/library/functions.html#next
    
"""