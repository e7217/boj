import sys

def main(input_):
    list_ = input_.split()
    text = ''
    for _ in list_:
        text += (_[::-1] + ' ') 
    return text.rstrip()

stack = sys.stdin.readline().rstrip()

for _ in range(int(stack)):
    input_ = sys.stdin.readline().rstrip()
    print(main(input_))