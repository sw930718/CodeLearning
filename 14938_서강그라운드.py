## 아이디어 참고 : https://gist.github.com/sujin-lee0909/1aa9ee39c395181c9a3709cd8fa323a6    
import sys
import heapq

# input 
N, M, R = map(int, sys.stdin.readline().split()) # N: 노드수, R: 간선수  
T = list(map(int, sys.stdin.readline().split()))

edges = {i: [] for i in range(1, N+1)} # 노드 1 ~ N 까지로 노드별 간선정보 딕셔너리 생성 
for _ in range(R):
    a, b, l = map(int, sys.stdin.readline().split()) # 지역번호, 그 지역번호와 연결된 다른 지역번호, 지역간 거리 
    # 양방향 
    edges[a].append((l, b)) 
    edges[b].append((l, a))

# code 
def maxItem(start):
    itemcnt = 0
     
    # distance[start][start] = 0
    INF = int(1e9)
    distance = ['INF' for _ in range(N + 1)]

    distance[start] = 0 
    h = edges[start].copy() # 얕은 복사 ! 주의. 이것 때문에 뒷노드 start 실행시 앞 노드의 영향 받아서 정답이 안나왔음  
    heapq.heapify(h)
    
    while h:
        length, a = heapq.heappop(h)
        if distance[a] == 'INF': 
            distance[a] = length
            for plus_length, i in edges[a]:
                if distance[i] == 'INF':
                    heapq.heappush(h, ((plus_length+length), i))
            
    
    for idx, values in enumerate(distance):
        if (values == 'INF') or (values > M):
            continue
        else:
            itemcnt += T[idx-1]
                
    return itemcnt

print(max([maxItem(i) for i in range(1,N+1)]))
