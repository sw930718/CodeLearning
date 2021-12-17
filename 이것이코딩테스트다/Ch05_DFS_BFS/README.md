# 탐색 알고리즘(DFS/BFS) 문제 정리

- 스택(stack) : 한쪽으로만 push & pop (선입후출 구조)
    - 별도 라이브러리 불필요 , 리스트로 선언 후 append() & pop() 함수 이용 
    - list[::-1] # 최상단 원소부터 출력
- 큐(que) : 한쪽으로 push & 다른쪽으로 pop (선입선출 구조)
    - 라이브러리 사용 (import collections import deque), 선언(deque()), append() & popleft() 함수 이용 
    - 역순출력(나중에 들어온 순서)시 .reverse() 실행 후 출력
- 재귀 함수 : 정의한 함수내에 자기자신(함수)호출 (반드시 if문으로 종료조건 작성해줘야함)

- DFS(Depth First Search) : 깊이우선탐색    
![예제](https://i.ibb.co/ZfGrLcy/IMG-764-A65-A40-C73-1.jpg)    
- BFS(Breath First Search) : 너비우선탐색   
![예제](https://i.ibb.co/T4jfvm9/IMG-AFA97-E85-AC54-1.jpg)    

- 프로그래밍내 그래프 표현 방식 (그래프도 다양: 무방향/방향, 가중치X/가중치O)
    - 1. 인접행렬 : 2차원 배열 이용해 연결관계 표현  

    INF = 999999999
    graph=[[0, 1, 1],
        [1, 0, INF],
        [1, INF, 0]]

    - 2. 인접리스트 : 리스트 이용해 연결관계 표현

    graph=[[] for _ in range(3)]

    graph[0].append(1)
    graph[0].append(2)
    graph[1].append(0)
    graph[2].append(0)

- Tip. 
