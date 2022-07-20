b=int(input("数字是："))
t=[]
while 1:
    x=b
    C=0
    if x%2==0:
        x=x/2
        print(b,C,x)
        C=C+1
    else :
        x=x*5+1
        print(b,C,x)
        C=C+1
    while not(x==1 or x==-1):   
        if x%2==0:
            x=x/2
            print(b,C,x)
            C=C+1
        else :
            x=x*5+1
            print(b,C,x)
            C=C+1
        t.append(x)
        if t.count(x)>1:
            break     
        if x==b:
            break
    print(t,"\n上为计算过程都为可进入此循环的数'") 
    z=input(str(b)+'过程次数'+str(C))
    if b<0:
        b=b-1
    if b>0:
        b=b+1
    t=[]
