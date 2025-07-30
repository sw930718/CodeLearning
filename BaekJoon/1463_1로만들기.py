import sys

sys.setrecursionlimit(1000000)  # 재귀 제한 열어주기 

input = sys.stdin.readline
N = int(input().rstrip())
visited = [1e6]*(N+1)
min_ops = 1e6


def rep(x,cnt):
    global min_ops
    if x==1:
        min_ops = min(min_ops, cnt)
        return 
    if visited[x] <= cnt: # 현재 위치까지의 최소값으로 저장된 값보다 지금 경우의 cnt값이 더 크거나 같으면 해당 경우 더 진행 X 
        return
    visited[x] = cnt
    
    if x % 3 == 0:
        rep(x // 3, cnt + 1)
    if x % 2 == 0:
        rep(x // 2, cnt + 1)
    rep(x - 1, cnt + 1)


rep(N, 0)
print(min_ops)
