from string import ascii_uppercase
def solution(s, n):
    answer=""
    
    alpha_list=list(ascii_uppercase)
    for i in s:
        if i==' ':
            answer+=" "
            continue
        num=ord(i)+n
        if (i.isupper() and 90<num) or (i.islower() and num>122):
            num-=26          

        answer+=(chr(num))
    return answer