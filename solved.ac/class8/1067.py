import sys

def main(b, c):
    b_ = b.split()
    c_ = c.split()
    result = 0
    for k, v in enumerate(b_):
        x = b_.pop()
        b_.insert(0, x)
        sum_ = 0
        for i in range(len(b_)):
            sum_ += int(b_[-(i+1)]) * int(c_[-(i+1)]) 
        if sum_ >= result:
            result = sum_
    return result

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
c = sys.stdin.readline().rstrip()

print(main(b,c))


