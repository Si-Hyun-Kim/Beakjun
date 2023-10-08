def RSP(i,n):
    val_list=list(i.values())
    if n>=len(i[1]):
        char_list=[item[-1] for item in val_list]
        if ('R' in char_list) and ('S' in char_list) and ('P' in char_list):
            print(0)
        elif char_list.count('R')==1 or char_list.count('S')==1 or char_list.count('P')==1:
            for j in char_list:
                if (j!='X') and ((j=='R') or (j=='S') or (j=='P')):
                    print(char_list.index(j)+1)
                    break    
        else:
            print(0)
    else:
        char_list=[item[n] for item in val_list]
        if ('R' in char_list) and ('S' in char_list) and ('P' in char_list):
            RSP(i,n+1)
        elif (char_list.count('R')+char_list.count('X')==len(char_list)) or (char_list.count('S')+char_list.count('X')==len(char_list)) or (char_list.count('P')+char_list.count('X')==len(char_list)):
            RSP(i,n+1)
        else:
            for win,lose in RPS_string:
                if (win in char_list) and (lose in char_list):
                    for j in char_list:
                        if j==lose:
                            p=char_list.index(j)
                            dict_index.append(p+1)
                            char_list[p]=''
                            for k in dict_index:
                                i[k]='X'*len(i[1])
                            dict_index.clear()
            RSP(i,n+1)
T=int(input())
robot=[]
RPS_string=(('R','S'),('S','P'),('P','R'))
dict_index=[]
for i in range(T):
    num={}
    N=int(input())
    for j in range(N):
        string=input()
        num[j+1]=string
    robot.append(num)
for i in robot:
    RSP(i,0)