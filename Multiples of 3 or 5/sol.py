def solution(max):
    return 0 if max < 3 else sum(3, max-1)+sum(5, max-1)-sum(15, max-1)


def sum(num, max):
    return (int(max/num)*int(max/num+1)/2)*num
