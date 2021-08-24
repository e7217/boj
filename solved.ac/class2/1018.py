x= [[1,1,1,1,-1,-1,-1,-1]
,[1,1,1,1,-1,-1,-1,-1]
,[1,1,1,1,-1,-1,-1,-1]
,[1,1,1,1,-1,-1,-1,-1]
,[1,1,1,1,-1,-1,-1,-1]
,[1,1,1,1,-1,-1,-1,-1]
,[1,1,1,1,-1,-1,-1,-1]
,[1,1,1,1,-1,-1,-1,-1]]

for k,v in enumerate(x):
    print(k, v)

listx = [1,1,1,1,1,1,-1,-1,-1]

def fill_board(list):
    sum = 0
    for i in range(8):
        if i % 2 == 0:
            list[i] = list[i] * (-1)
        else:
            list[i] = list[i] * (1)
        sum += list[i]
    return sum

def fill_board2(list):
    sum = 0
    for i in range(8):
        if i % 2 == 1:
            list[i] = list[i] * (-1)
        else:
            list[i] = list[i] * (1)
        sum += list[i]
    return sum

u = fill_board(listx)
print(u)