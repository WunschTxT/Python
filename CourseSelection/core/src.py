from core import admin, student, teacher

choice_dic = {'1': admin.admin_main,
              '2': teacher.teacher_main,
              '3': student.student_main}


def run():
    while True:
        print("""
---------------选课系统---------------
            1.管理员视图
            2.教师视图
            3.学生视图
            q.退出
        """)
        choice = input("请输入要选择的功能：").strip()
        if choice == 'q':
            break
        elif choice in choice_dic:
            choice_dic[choice]()
        else:
            continue
