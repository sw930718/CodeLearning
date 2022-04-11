def solution(dartResult):
    option=['*','#']
    multifly=['S','D','T']

    answer=[]

    for i, score in enumerate(dartResult):
        if score in option:
            if score == '*': # '*'이 나온경우 
                star_now=int(answer.pop())*2
                if len(answer)!=0:
                    star_pre=int(answer.pop())*2
                    answer.append(star_pre)
                answer.append(star_now)

            elif score == '#': # '#'이 나온경우 
                star_now=int(answer.pop())*(-1)
                answer.append(star_now)

        elif score in multifly:
            if score == 'S':
                star_now=int(answer.pop())**1
                answer.append(star_now)
            elif score == 'D':
                star_now=int(answer.pop())**2
                answer.append(star_now)
            elif score == 'T':
                star_now=int(answer.pop())**3
                answer.append(star_now)

        else:
            if score == '0' : #10 인 경우 
                answer.pop()
                answer.append(10)
            else:
                answer.append(int(score))

    return sum(answer)
