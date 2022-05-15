import math
def solution(n):
    num=math.sqrt(n)
    if num.is_integer():
        return pow(int(num)+1,2)
    else:
        return -1