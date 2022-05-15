def solution(numbers):
    num=[i for i in range(10)]
    for i in numbers:
        num.remove(i)
    return sum(num)