tall = ""
weight = ""

def inp():
    global tall
    tall = input("请输入您的身高（m）：")
    tall.strip()
    global weight
    weight = input("请输入您的体重（kg）：")
    weight.strip()
    return

def sub():
    global tall, bmi
    global weight
    print("\n" + "="*10 + "计算BMI指数" + "="*10)
    try:
        tall = float(tall)
        weight = float(weight)
        bmi = weight / (tall * tall)
    except ValueError:
        print("您输入的不是数字，请重新输入！\n")
        inp()
        sub()
    if bmi < 20:
        print("\n您的BMI指数为：", bmi, "\n\n您太瘦了")
    elif 20 <= bmi <= 25:
        print("\n您的BMI指数为：", bmi, "\n\n您很健康")
    else:
        print("\n您的BMI指数为：", bmi, "\n\n您太胖了")
    return

inp()
sub()
