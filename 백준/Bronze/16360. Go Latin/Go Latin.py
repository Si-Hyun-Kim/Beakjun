num=int(input())
word_list=[]
Eng_Latin=(('a','as'),('i','ios'),('y','ios'),('l','les'),
           ('n','anes'),('o','os'),('r','res'),('t','tas'),
           ('u','us'),('v','ves'),('w','was'))
Eng=('a','i','y','l','n','o','r','t','u','v','w')
for i in range(num):
    word=input()
    word_list.append(word)
for i in word_list:
    for j,k in Eng_Latin:
        a=word_list.index(i)
        if i[-1]==j:
            word_list[a]=i[0:-1]+k
            break
        elif i[-2:]=='ne':
            word_list[a]=i[0:-2]+'anes'
            break
        if i[-1] not in Eng:
            word_list[a]=i+'us'
            break
for i in word_list:
    print(i)