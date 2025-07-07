import sys 

def dfs(graph, v, visited):
    visited=[False]*(N+1)
    
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)  
    return
    
def gravity(graph):
    for col in range(N):
        for row in range(N-1,-1,-1):
            if graph[col][row] >= 0:
                for k in range(col+1, N+1):
                    if k==N or graph[k][row] >= -1:
                        graph[col][row], graph[k-1][row] = graph[k-1][row], graph[col][row]
                        break
                    
def search():
    max = 0
    
    for _ in range(turn):
        dfs(garage[(N*turn - N):][:])
        gravity(garage)
        # ? - 직사각형 구하는 방법 
        
    return max

if __name__ == "__main__":
    # input
    N = int(sys.stdin.readline())
    
    turn = 3 
    garage = []
    for _ in range(N*turn):
        garage.append(list(map(int, sys.stdin.readline().split())))
        
    # code 
    print(search())