n = 3
a = [[str(n) for n in input().split()]for __ in range(n)]
for i in range(3) :
    if (a[i][0] == a[i][1] == a[i][2]) :
        if a[i][0] == 'X' or a[i][0] == 'O' :
            print(f'{a[i][0]} wins')
            break
        else :
            print('Draw')
            break
    elif (a[0][i] == a[1][i] == a[2][i]) :
        if a[0][i] == 'X' or a[0][i] == 'O' :
            print(f'{a[0][i]} wins')
            break
        else :
            print('Draw')
            break
    elif (a[0][0] == a[1][1] == a[2][2]) or (a[0][2] == a[1][1] == a[2][0]) :
        if a[1][1] == 'X' or a[1][1] == 'O' :
            print(f'{a[1][1]} wins')
            break
        else :
            print('Draw')
            break
    else :
        print('Draw')
        break
