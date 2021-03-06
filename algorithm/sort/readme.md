# 정렬 알고리즘

#### 각 알고리즘 시간 복잡도
+ 버블 - O(n^2^)
+ 선택 - O(n^2^)
+ 삽입 - O(n^2^)
+ 병합 - O(nlog n)
+ 퀵 - O(nlog n)

#### 선택 정렬
+ 시간 복잡도 : O(N^2^)
  
전체 요소 중 최저값을 탐색한 뒤, 앞으로 정렬.
나머지 값에 대해서 동일한 작업 수행
요소의 길이만큼 작업

#### 삽입 정렬
+ 시간 복잡도 : O(N^2^)

해당 원소를 정렬한 리스트의 적절한 위치에 삽입
이미 수행한 리스트들에 대해서는 정렬이 되어있다고 여김

#### 퀵 정렬
+ 시간 복잡도 : O(nlog n)

기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식
큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 기준 = Pivot(피벗)
(호어 분할 방식) 리스트에서 첫 번째 데이터를 피벗으로 선정
왼쪽에서부터 피벗보다 작은 값 탐색, 오른쪽에서부터 피벗보다 큰 값 탐색
=> 서로 교환
탐색 시, 서로 교차하는 경우에는 최소값 탐색의 위치와 피벗의 위치 교환
=> 이 때 피벗의 왼쪽 리스트는 피벗보다 작고 오른쪽 리스트는 피벗보다 크다는 특징을 가짐
각 리스트에 대해서 다시 피벗 설정하여 동일 작업 수행
종료 조건: 잔여 갯수가 1개일 때.