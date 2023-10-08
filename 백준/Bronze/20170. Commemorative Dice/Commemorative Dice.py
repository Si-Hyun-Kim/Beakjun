def gcd(a,b):
    if b==0: return a
    return gcd(b,a%b)
dice1=list(map(int,input().split()))
dice2=list(map(int,input().split()))
per=0
total=0
for i in dice1:
    for j in dice2:
        total+=1
        if i>j:
            per+=1
g=gcd(per,total)
print('{}/{}'.format(per//g,total//g))