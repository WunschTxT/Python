from db import modules


def student_register_interface(name, password):
    student_obj = modules.Student.get_obj_name(name)
    if student_obj:
        return False, '学生已存在'
    else:
        modules.Student(name, password)
        return True, '学生注册成功'


def check_all_course(stu_name):
    # 选课时查看所有课程
    stu_obj = modules.Student.get_obj_name(stu_name)
    if stu_obj.school:
        school_obj = modules.School.get_obj_name(stu_obj.school)
        if school_obj.course_list:
            return True, school_obj.course_list
        else:
            return False, '该学校暂无课程'
    else:
        return False, '您还没选择学校'


def choose_school_interface(student_name, school_name):
    obj = modules.Student.get_obj_name(student_name)
    if obj.school:
        return False, '你已选择学校，无法再次选择！'
    else:
        obj.choose_school(school_name)
        return True, f'{student_name}选择{school_name}学校成功'


def choose_course_interface(student_name, course_name):
    stu_obj = modules.Student.get_obj_name(student_name)
    if course_name in stu_obj.coures_list:
        return False, '你已选择课程，无法再次选择！'
    stu_obj.add_course(course_name)
    course_obj = modules.Course.get_obj_name(course_name)
    course_obj.add_sutdent(student_name)
    return True, f'{student_name}选择{course_name}学校成功'


def check_score_interface(student_name):
    obj = modules.Student.get_obj_name(student_name)
    return obj.score


def check_student_course(student_name):
    # 查看已选课程
    obj = modules.Student.get_obj_name(student_name)
    if obj.course_list:
        return True, obj.stu_tell_info()
    else:
        return False, '暂无课程，请先选择课程'
