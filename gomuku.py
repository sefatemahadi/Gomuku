board =[]
for i in range(10):
    board.append('----------')

def evf():
    for _str in board:
        if 'xxxxx' in _str:
            return 100
        if 'ooooo' in _str:
            return -100
        if ('xxxx-' or '-xxxx' or 'xxx-x' or 'xx-xx' or 'x-xxx') in _str:
            return 40
        if ('oooo-' or '-oooo' or 'ooo-o' or 'oo-oo' or 'o-ooo') in _str:
            return -40
        if ('xxx--' or '-xxx-' or '--xxx') in _str:
            return 30
        if ('ooo--' or '-ooo-' or '--ooo') in _str:
            return -30

    strings =[]

    for i in range(10):
        _str =''
        for j in range(10):
            _str+=board[j][i]
        strings.append(_str)

    _str =''
    for i in range(10):
        _str+=board[i][i]

    strings.append(_str)

    strings.append(board[0][1]+board[1][2]+board[2][3]+board[3][4]+board[4][5]+board[5][6]+board[6][7]+board[7][8]+board[8][9])
    strings.append(board[0][2]+board[1][3]+board[2][4]+board[3][5]+board[4][6]+board[5][7]+board[6][8]+board[7][9])
    strings.append(board[0][3]+board[1][4]+board[2][5]+board[3][6]+board[4][7]+board[5][8]+board[6][9])
    strings.append(board[0][4]+board[1][5]+board[2][6]+board[3][7]+board[4][8]+board[4][9])
    strings.append(board[0][5]+board[1][6]+board[2][7]+board[3][8]+board[4][9])

    strings.append(board[1][0]+board[2][1]+board[3][2]+board[4][3]+board[5][4]+board[6][5]+board[7][6]+board[8][7]+board[9][8])
    strings.append(board[2][0]+board[3][1]+board[4][2]+board[5][3]+board[6][4]+board[7][5]+board[8][6]+board[9][7])
    strings.append(board[3][0]+board[4][1]+board[5][2]+board[6][3]+board[7][4]+board[8][5]+board[9][6])
    strings.append(board[4][0]+board[5][1]+board[6][2]+board[7][3]+board[8][4]+board[9][5])
    strings.append(board[5][0]+board[6][1]+board[7][2]+board[8][3]+board[9][4])

    _str =''
    for i in range(9,-1,-1):
        _str+=board[i]

    strings.append(_str)

    strings.append(board[0][8]+board[1][7]+board[2][6]+board[3][5]+board[4][4]+board[5][3]+board[6][2]+board[7][1]+board[8][0])
    strings.append(board[0][7]+board[1][6]+board[2][5]+board[3][4]+board[4][3]+board[5][2]+board[6][1]+board[7][0])
    strings.append(board[0][6]+board[1][5]+board[2][4]+board[3][3]+board[4][2]+board[5][1]+board[6][0])
    strings.append(board[0][5]+board[1][4]+board[2][3]+board[3][2]+board[4][1]+board[5][0])
    strings.append(board[0][4]+board[1][3]+board[2][2]+board[3][1]+board[4][0])

    strings.append(board[1][9]+board[2][8]+board[3][7]+board[4][6]+board[5][5]+board[6][4]+board[7][3]+board[8][2]+board[9][1])
    strings.append(board[2][9]+board[3][8]+board[4][7]+board[5][6]+board[6][5]+board[7][4]+board[8][3]+board[9][2])
    strings.append(board[3][9]+board[4][8]+board[5][7]+board[6][6]+board[7][5]+board[8][4]+board[9][3])
    strings.append(board[4][9]+board[5][8]+board[6][7]+board[7][6]+board[8][5]+board[9][4])
    strings.append(board[5][9]+board[6][8]+board[7][7]+board[8][6]+board[9][5])

    for _str in strings:
        if 'xxxxx' in _str:
            return 100
        if 'ooooo' in _str:
            return -100
        if ('xxxx-' or '-xxxx' or 'xxx-x' or 'xx-xx' or 'x-xxx') in _str:
            return 40
        if ('oooo-' or '-oooo' or 'ooo-o' or 'oo-oo' or 'o-ooo') in _str:
            return -40
        if ('xxx--' or '-xxx-' or '--xxx') in _str:
            return 30
        if ('ooo--' or '-ooo-' or '--ooo') in _str:
            return -30
    return 0

def coordinate(icor,jcor):
    icor0,icor1 =0,9
    jcor0,jcor1 =0,9

    if icor:
        icor0 = icor
        for i in range(4):
            icor0 = icor0 - 1
            if not icor0:
                break

    if icor != 9:
        icor1 = icor
        for i in range(4):
            icor1 = icor1 + 1
            if icor1 == 9:
                break

    if jcor:
        jcor0 = jcor
        for i in range(4):
            jcor0 = jcor0 - 1
            if not jcor0:
                break

    if jcor != 9:
        jcor1 = jcor
        for i in range(4):
            jcor1 = jcor1 + 1
            if jcor1 == 9:
                break
    return icor0,icor1,jcor0,jcor1

def correct(icor,jcor):
    if (0 <= icor <= 9) and (0 <= jcor <= 9):
        return 1
    return 0

def rep_char_in_string(string,index,char):
    return string[:index]+char+string[index+1:]

def reform_string(string,index):
    return string[:index]+'-'+string[index+1:]

def minimax(icor0,icor1,jcor0,jcor1,turn,depth,count,alpha,beta):
    #print_board()
    check =evf()

    if check:
        return check

    # if count == 100 or depth == 3:
    #     return 0

    if count == 100:
        return 0

    if 0 < count <= 25:
        if depth == 3:
            return 0

    if 25 < count <= 35:
        if depth == 4:
            return 0

    if 35 < count <= 50:
        if depth == 5:
            return 0

    if turn:
        best =-1000
        for i in range(icor0, icor1 + 1):
            for j in range(jcor0, jcor1 + 1):
                if board[i][j] == '-':
                    board[i] =rep_char_in_string(board[i],j,'x')
                    count+=1
                    best =max(best,minimax(icor0,icor1,jcor0,jcor1,0,depth+1,count,alpha,beta))
                    board[i] =reform_string(board[i],j)
                    count-=1
                    alpha =max(alpha,best)

                    if beta <= alpha:
                        break
        return best

    if not turn:
        best =1000
        for i in range(icor0, icor1 + 1):
            for j in range(jcor0, jcor1 + 1):
                if board[i][j] == '-':
                    board[i] =rep_char_in_string(board[i],j,'o')
                    count+=1
                    best =min(best,minimax(icor0,icor1,jcor0,jcor1,1,depth+1,count,alpha,beta))
                    board[i] =reform_string(board[i],j)
                    count-=1
                    beta =min(beta,best)

                    if beta <= alpha:
                        break
        return best

def moves(icor0,icor1,jcor0,jcor1):
    count =0
    for i in range(icor0,icor1+1):
        for j in range(jcor0,jcor1+1):
            if board[i][j] != '-':
                count+=1
    return count

def computer(icor,jcor,count):
    best = -1000
    imove,jmove =0,0

    imoves = [1, -1, 0, 0, 1, -1, -1, 1, 2, -2, 0, 0, 2, -2, 2, -2]
    jmoves =[0, 0, 1, -1, 1, -1, 1, -1, 0, 0, 2, -2, 2, -2, -2, 2]

    icor0,icor1,jcor0,jcor1 =coordinate(icor,jcor)

    if moves(icor0,icor1,jcor0,jcor1) <= 4:
        from random import randint
        while True:
            i =randint(1,15)
            if correct(icor+imoves[i],jcor+jmoves[i]) and board[icor+imoves[i]][jcor+jmoves[i]] == '-':
                print ('random move:',icor+imoves[i],jcor+jmoves[i])
                board[icor+imoves[i]] =rep_char_in_string(board[icor+imoves[i]],jcor+jmoves[i],'x')
                count+=1
                return count

    for i in range(icor0,icor1+1):
        for j in range(jcor0,jcor1+1):
            if board[i][j] == '-':
                board[i] =rep_char_in_string(board[i],j,'x')
                count+=1
                temp =minimax(icor0,icor1,jcor0,jcor1,0,1,count,-10000,10000)
                if temp > best:
                    best =temp
                    imove =i
                    jmove =j
                board[i] =reform_string(board[i],j)
                count-=1
    board[imove] = rep_char_in_string(board[imove], jmove, 'x')
    count += 1
    return count

def human():
    print('Enter coordinates:')
    i =int(input())
    j =int(input())
    board[i] =rep_char_in_string(board[i],j,'o')
    return i,j

def print_board():
    for i in range(10):
        print(board[i])
    print()

count =0
while True:
    i,j =human()
    print_board()
    count+=1
    count =computer(i,j,count)
    print_board()