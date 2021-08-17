import sys

def main(list, input_):
    text = input_.split()
    if text[0] == 'push':
        list.append(int(text[1]))
    elif text[0] == 'size':
        print(len(list))
    elif text[0] == 'empty':
        if list:
            print(0)
        else:
            print(1)
    elif text[0] == 'top':
        if list:
            print(list[-1])
        else:
            print(-1)
    elif text[0] == 'pop':
        if list:
            print(list[-1])
            list.pop()
        else:
            print(-1)
    return list        

stack = int(sys.stdin.readline().rstrip())

list_ = []
for _ in range(stack):
    input_ = sys.stdin.readline().rstrip()
    list_ = main(list_, input_)
