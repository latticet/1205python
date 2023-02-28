# 用户登录和注册

# 接收用户选择功能
code = input('选择功能【1注册|2登录】：')

if code == '1':
    # 接收用户注册信息
    username = input('用户名：')
    password = input('密  码：')

    # 将注册信息写入user.txt
    # 打开文件-a
    f = open('resource/user.txt', mode='a', encoding='utf8')

    # 写入文件
    f.write(f'{username},{password}\n')

    # 关闭文件
    f.close()
    print('注册成功！')
else:
    # 接收用户注册信息
    username = input('用户名：')
    password = input('密  码：')

    # 打开文件
    f = open('resource/user.txt', encoding='utf8')
    # 读取内容
    userinfo_list = f.readlines()
    for userinfo in userinfo_list:
        # 判断文件的用户信息和用户输入的是否相等
        if userinfo.rstrip('\n') == f'{username},{password}':
            print(f'【{username}】登录成功')
            break
    else:
        print('用户名或密码错误')

    # 关闭文件
    f.close()
