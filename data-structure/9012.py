import sys

def main(input_):
    x = 0
    for _ in input_:
        if _ == '(':
            x += 1
        else:
            x += -1
        if x == -1:
            return 'NO'
    if x == 0:
        return 'YES'
    else:
        return 'NO'
    

a = sys.stdin.readline().rstrip()
for _ in range(int(a)):
    print(main(sys.stdin.readline().rstrip()))