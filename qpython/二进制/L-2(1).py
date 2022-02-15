#获取需求
file = input('请定义文件名称：')
while len(file)==False:
    print('文件名称不能为空！')
    file = input('请定义文件名称：')
character = input('请输入生成密码所需要的字符：')
while len(character) == False:
    print('生成密码所需要的字符不能为空！')
    character = input('请输入生成密码所需要的字符：')
Minimum_length = int(input('请输入最小密码长度：'))
while Minimum_length <= 0 :
    print('密码长度不能小于1')
    Minimum_length = int(input('请输入密码长度：'))
Maximum_length=int(input('请输入最大密码长度：'))
while Maximum_length<Minimum_length:
    print('最大密码长度不能小于最小密码长度！')
    Maximum_length=int(input('请输入最大密码长度：'))
file1 = open(file, 'w')
#生成python字典
list1 = list(character)
list2 = [x for x in range(len(list1))]
Key_array = dict(zip(list2,list1))
#算法
key = []
max_key =[]
while len(max_key) != Minimum_length:
    max_key.append(list2[len(list2)-1])
while len(key) != Minimum_length:
    key.append(0)
while True:
    for i in list2:

        key[0]=i
        password=[]
        for h in key:
            password.append(Key_array.get(h))
        psswd = ''.join(password)  # 去除多余符号
        print(key)
        file1.write(psswd)
        file1.write("\r")
#算法
        if key[0]==max_key[0]:
           for j in range(len(key)):
               if key[j]!=max_key[0]:
                    key[j]=key[j]+1
                    key[j-1]=0
                    break
        if key==max_key:
            break
    if key==max_key:
        break
if Maximum_length != Minimum_length:
    while len(key) != Maximum_length:
        for h in range(0, len(key)):
            key[h] = 0
        key.append(0)
        max_key.append(list2[len(list2)-1])
        while True:
            for i in list2:
                key[0] = i
                password = []
                for h in key:
                    password.append(Key_array.get(h))
                psswd = ''.join(password)  # 去除多余符号
                print(psswd)
                file1.write(psswd)
                file1.write("\r")
                # 算法
                if key[0] == max_key[0]:
                    for j in range(len(key)):
                        if key[j] != max_key[0]:
                            key[j] = key[j] + 1
                            key[j - 1] = 0
                            break
                if key == max_key:
                    break
            if key == max_key:
                break
