def is_isogram(s):
    return len(list(s.lower())) == len(set(s.lower()))
