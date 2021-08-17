# 자료구조
last update 2021.08.17
* * *
#### 10828
+ 문자열 입력 시, input()을 쓰는 것보다 컴퓨터 리소스를 적게 사용한다
```python
import sys

input = sys.stdin.readline().rstrip()
```
#### 9093
+ 문자열 뒤집기
```python
string = 'abcd'
string[::-1]
# 'bcda'
```
