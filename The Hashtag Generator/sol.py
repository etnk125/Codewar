def generate_hashtag(s):
    ls = "".join(i.capitalize() for i in s.split())
    return False if len(ls) > 139 or len(ls) == 0 else "#"+ls
