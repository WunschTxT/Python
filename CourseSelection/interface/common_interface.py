from conf import settings
from db import modules
import os
from lib import common


def login_interface(user_type, name, password):
    # 公共：登陆接口
    if user_type == 'admin':
        obj = modules.Admin.get_obj_name(name)
    elif user_type == 'teacher':
        obj = modules.Teacher.get_obj_name(name)
    elif user_type == 'student':
        obj = modules.Student.get_obj_name(name)
    else:
        return False, '用户类型不存在！'
    if obj:
        if obj.password == password:
            return True, f'{user_type}:{name}登陆成功'
        else:
            return False, '密码错误'
    else:
        return False, '用户不存在'


def check_all_school():
    path = os.path.join(settings.DB_PATH, 'school')
    return common.get_all_obj(path)


def check_all_course():
    path = os.path.join(settings.DB_PATH, 'course')
    return common.get_all_obj(path)
