tree=list(input())
node=-1
nodes=[]
for i in range(len(tree)):
    if tree[i]=='(':
        node+=1
    else:
        if tree[i-1]=='(':
            nodes.append(node)
        node-=1
print(sum(nodes))