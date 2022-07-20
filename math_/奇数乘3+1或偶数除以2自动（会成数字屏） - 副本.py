gc=[]
n=0
y=0
g=0
shu=(int(input("上次试到数字是（没有为零）：")))+1
shuu=shu
while True:
    if shuu%2==0:
        shuu=int(shuu/2)
        g+=1
    else:
        shuu=int(shuu*3+1)
        g+=1
    gc.append(shuu)
    while not(shu==shuu or shuu==1):
        if shuu%2==0:
            shuu=int(shuu/2)
            g+=1
        else:
            shuu=int(shuu*3+1)
            g+=1
        gc.append(shuu)
    if shuu==1:
        n=n+1
        print ("n数",shu,"失败 已成功",y,"次 已失败",n,"次 过程次数",g)
        shu=shu+1
        shuu=shu
        gc=[]
        g=0
    else :
        y=y+1
        print ("y数",shu,"成功 已成功",y,"次 已失败",n,"次 过程次数",g)
        shu=shu+1
        shuu=shu
        gc=[]
        g=0
        x=(wc)

