from db import modules


def choose_course_interface(teacher_name, course_name):
    # 老师：选择课程接口
    obj = modules.Teacher.get_obj_name(teacher_name)
    if course_name in obj.coures_list:
        return False, '课程已选无需再次选择'
    else:
        obj.add_course(course_name)
        return True, f'{teacher_name}选择课程{course_name}成功'


def teacher_check_course(teacher_name):
    # 教师查看课程接口
    obj = modules.Teacher.get_obj_name(teacher_name)
    if not obj.course_list:
        return False, '没有课程', None
    else:
        return True, obj.tea_tell_info, obj.course_list


def teacher_check_student(course_name):
    # 教师查看学生接口
    course_obj = modules.Course.get_obj_name(course_name)
    if not course_obj.student.list:
        return False, '暂无学生'
    return True, course_obj.student_list


def mark_student_interface(teacher_name, student_name, course_name, score):
    # 教师为学生打分接口
    teacher_obj = modules.Teacher.get_obj_name(teacher_name)
    student_obj = modules.Student.get_obj_name(student_name)
    teacher_obj.mark_studnet(student_obj, course_name, score)
    return f'{teacher_name}修改{student_name}的{course_name}分数为{score}'