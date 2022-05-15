import math
from itertools import permutations

def solution(numbers):
    
    def prime_num(n):
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i == 0:
                return False
        return True
    
    answer = set()
    
    num_lst=list(numbers)
    for cnt in range(1,len(num_lst)+1):
        nums=set(permutations(num_lst,cnt))
        for num in nums:
            n=int(''.join(num))
            if n>1 and prime_num(n):
                answer.add(n)
            
    return len(answer)