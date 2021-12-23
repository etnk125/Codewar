def order(sentence):
    ls = sentence.split(' ')
    ls.sort(key=findNum)
    return " ".join(ls)


def findNum(e):
    for i in e:
        if i.isdigit():
            return i


"""
    def order(words):
        return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
    
    sorted -->เรียงเลข

    def order(sentence):
        return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

    filter เอา
"""
