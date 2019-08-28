from db import modules


def admin_register_interface(name, password):
    admin_obj = modules.Admin.get_obj_name(name)
    if admin_obj:
        return False, '管理员以存在'
    else:
        modules.Admin(name, password)
        return True, '管理员注册成功'


def create_school_interface(admin, school_name, addr):
    # 创建学校接口
    school_obj = modules.School.get_obj_name(school_name)
    if school_obj:
        return False, '学校已存在'
    else:
        admin_obj = modules.Admin.get_obj_name(admin)
        admin_obj.create_school(school_name, addr)
        return True, f'{admin}:{school_name}创建学校成功！'


def create_teacher_interface(admin, teacher_name, password='123'):
    teacher_obj = modules.Teacher.get_obj_name(teacher_name)
    if teacher_obj:
        return False, '教师已存在'
    else:
        admin_obj = modules.Admin.get_obj_name(admin)
        admin_obj.create_teacher(teacher_name, password)
        return True, f'{admin}:{teacher_name}学校创建成功！'


def create_course_interface(admin, course_name, price, period, school_name):
    course_obj = modules.Course.get_obj_name(course_name)
    if course_obj:
        return False, '该课程已存在'
    else:
        admin_obj = modules.Admin.get_obj_name(admin)
        admin_obj.create_course(course_name, price, period)

        school_obj = modules.School.get_obj_name(school_name)
        school_obj.add_course(course_name)
        return True, f'{admin}:{course_name}课程创建成功!'
