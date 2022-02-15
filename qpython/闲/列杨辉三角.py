def b():
    try:
        l1=[1,1]
        g=int(input("\n请问输出几行杨辉三角呢?\n请输入:"))
        if g<=0:
            print("请输入正常的数!")
            raise TypeError
        elif g==1:
            print("[1]")
        else:
            g-=2
            def a(l):
                b=len(l)
                l2=[]
                for j in range(b-1):
                    o=l[j]+l[j+1]
                    l2.append(o)
                l=[1]+l2+[1]
                return l
            print("[1]\n{}".format(l1))
            for y in range(g):
                l1=a(l1)
                print(l1)
    except:
        print("请输入数字!\n----------------------------")
        return b()
b()

