from core import src
from interface import common_interface, teacher_interface
from lib import common


teacher_info = {
    'name': None
}


def teacher_login():
    print('教师界面'.center(40, '-'))
    if teacher_info['name']:
        print('您已登录，无需再登录')
        return
    while True:
        name = input('请输入名字：').strip()
        password = input('请输入密码：').strip()
        if not name or not password:
            continue
        state, msg = common_interface.login_interface('teacher', name, password)
        if state:
            print(msg)
            teacher_info['name'] = name
            break
        else:
            print(msg)


def choose_course():
    print('选择课程'.center(40, '-'))
    course_list = common_interface.check_all_course()
    if course_list is None:
        print('暂无课程')
    else:
        for i, course in enumerate(course_list):
            print(f'{i}:{course_list}')
        choice = input('请输要选择的课程：').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice >= len(course_list):
                return
            state, msg = teacher_interface.choose_course_interface(teacher_info['name', course_list(choice)])
            if state:
                print(msg)
            else:
                print(msg)
        else:
            print('请输入数字')


def check_course():
    # 查看课程
    print('查看课程'.center(40, '-'))
    state, course_list, _ = teacher_interface.teacher_check_course(teacher_info['name'])
    if state:
        pass
    else:
        print(course_list)


def check_student():
    print('查看学生'.center(40, '-'))
    _,_,course_list = teacher_interface.teacher_check_course(teacher_info['name'])
    if not course_list:
        return
    for i, course in enumerate(course_list):
        print(f"{i}:{course}")
    choice = input('请选择课程：').strip()
    if choice.isdigit():
        choice = int(choice)
        if choice >= len(course_list):
            print('你输入的超过选择范围')
        else:
            state, student_list = teacher_interface.teacher_check_student(course_list[choice])
            if state:
                for i, k in enumerate(student_list):
                    print(f'{i}:学生 {k}')
            else:
                print(course_list)
    else:
        print('请输入数字！')


def mod_student_score():
    print('为学生打分'.center(40, '-'))
    _, _, course_list = teacher_interface.teacher_check_course(teacher_info['name'])
    if not course_list:
        print('暂无课程，请先去选择课程')
        return
    while True:
        for i, j in enumerate(course_list):
            print(f"{i}:{course_list}")
            choice = input('请选择课程：').strip()
            if choice.isdigit():
                choice = int(choice)
                if choice >= len(course_list):
                    print('你输入的超过选择范围')
                else:
                    state, student_list = teacher_interface.teacher_check_student(course_list[choice])
                    if state:
                        for i, k in enumerate(student_list):
                            print(f'{i}:学生 {k}')
                            choice_stu = input('请选择要修改的学生：').strip()
                            if choice_stu.isdigit():
                                choice_stu = int(choice_stu)
                                if choice_stu >= len(student_list):
                                    print('你输入的超过选择范围')
                                else:
                                    score = input('请输入要修改的分数').strip()
                                    if score.isdigit():
                                        msg = teacher_interface.mark_student_interface(teacher_info['name'], student_list[choice_stu],course_list[choice])
                                        print(msg)
                                        break
                                    else:
                                        print('请输入数字！')
                            else:
                                print('请输入数字！')
                        else:
                            print(student_list)
            else:
                print('请输入数字！')


choice_dict = {
    '1': teacher_login,
    '2': choose_course,
    '3': check_course,
    '4': check_student,
    '5': mod_student_score
}


def teacher_main():
    while True:
        print('教师界面'.center(40, '-'))
        print('''
               1. 登录
               2. 选择课程
               3. 查看课程
               4. 查看学生
               5. 修改学生成绩
               q. 退出
            ''')
        choice = input('请选择功能：').strip()
        if choice == 'q':
            break
        elif choice in choice_dict:
            choice_dict[choice]()
        else:
            continue
