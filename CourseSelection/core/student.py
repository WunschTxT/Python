from interface import student_interface,common_interface
from db import modules
student_info = {'name': None}


def student_register():
    print('学生注册'.center(40, '-'))
    if student_info['name']:
        print('您已登陆，无法注册！')
        return
    while True:
        name = input('请输入姓名：').strip()
        password = input('请输入密码：').strip()
        passwordre = input('请确认密码：').strip()
        if not name or not password or not passwordre:
            continue
        if password == passwordre:
            state, msg = student_interface.student_register_interface(name, password)
            if state:
                print(msg)
                break
            else:
                print(msg)
                break
        else:
            print('两次密码不一致！')


def student_login():
    print('学生登陆'.center(40, '-'))
    if student_info['name']:
        print('您已登陆，无需再登陆！')
        return
    while True:
        name = input('请输入姓名：').strip()
        password = input('请输入密码：').strip()
        if not name or not password:
            continue
        state, msg = common_interface.login_interface('student', name, password)
        if state:
            print(msg)
            student_info['name'] = name
            break
        else:
            print(msg)
            break


def choose_school():
    # print('选择学校'.center(40, '-'))
    # while True:
    #     school_list = common_interface.check_all_school()
    #     if school_list:
    #         for i, school in enumerate(school_list):
    #             print(f'{i}:{school}')
    #         choice = input('请选择学校：').strip()
    #         if choice.isdigit():
    #             choice = int(choice)
    #             if choice >= len(school_list):
    #                 continue
    #             state, msg = student_interface.choose_school_interface(student_info['name'], school_list[choice])
    #             if state:
    #                 print(msg)
    #                 break
    #             else:
    #                 print(msg)
    #                 break
    #         else:
    #             print('请输入正确选择！')
    #     else:
    #         print('暂无学校')
    #         break
    print('选择学校'.center(40, '-'))
    while True:
        school_list = common_interface.check_all_school()
        if school_list:
            for i, school in enumerate(school_list):
                print('%s : %s' % (i, school))
            choice = input('请选择(学校)：').strip()
            if choice.isdigit():
                choice = int(choice)
                if choice >= len(school_list):
                    continue
                state, msg = student_interface.choose_school_interface(student_info['name'], school_list[choice])
                if state:
                    print(msg)
                    break
                else:
                    print(msg)
                    break
            else:
                print('请输入数字')
        else:
            print('暂无学校')
            break


def choose_course():
    print('选择课程'.center(40, '-'))
    while True:
        state, course_list = student_interface.check_all_course(student_info['name'])
        if state:
            for i, course in course_list:
                print(f'{i}:{course}')
            choice = input('请选择课程：').strip()
            if choice.isdigit():
                choice = int(choice)
                if choice >= len(course_list):
                    continue
                state, msg = student_interface.choose_course_interface(student_info['name'], course_list[choice])
                if state:
                    print(msg)
                    break
                else:
                    print(msg)
                    break
            else:
                print('请输入正确的选择！')



def check_score():
    print('查看分数'.center(40, '-'))
    score_dict = student_interface.check_score_interface(student_info['name'])
    for i, j in score_dict.items():
        print(f'课程:{i}\n分数：{j}')


def check_course():
    print('查看班级'.center(40, '-'))
    course_list = student_interface.check_student_course(student_info['name'])
    for i, coures in course_list:
        print()



choice_dict = {
    '1': student_register,
    '2': student_login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score,
    '6': check_course

}


def student_main():
    while True:
        print('学生界面'.center(40,'-'))
        print('''
               1. 注册
               2. 登录
               3. 选择学校
               4. 选择课程
               5. 查看分数
               6. 查看课程
               q. 退出
            ''')
        choice = input('请选择功能：').strip()
        if choice == 'q':
            break
        elif choice in choice_dict:
            choice_dict[choice]()
        else:
            continue

