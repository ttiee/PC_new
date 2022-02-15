#Cu Fe编写
def s():
    try:
        print("\n请问需要多少以内的质数？\n")
        m=int(input("请输入:"))
        if m>=2:
            c=m+1
            print("\n您需要的质数为以下这些:")
            print("2")
            t=1
            for a in range(1,c,2):
                i=0
                for b in range(2,a):
                    if a%b==0:
                        break
                    if a%b!=0:
                        i+=1
                if i==a-2:
                    print(a)
                    t+=1
            print("\n经我仔细地数过后总共有"+str(t)+"个质数\n")
            print("程序完成!\n打完收工!")
        else:
            print("抱歉哦，没有质数")
            raise ValueError
    except:
        print("请输入正确的格式!")
        print("重来!\n")
        print("-----------------------------------")
        return s()
s()