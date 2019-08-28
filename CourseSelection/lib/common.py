import os
from conf import settings

#验证登录的装饰器

def login_auth(user_type):
    from core import admin, teacher, student
    def validation(func):

        def wrapper(*args, **kwargs):
            if user_type == 'admin':
                if not admin.admin_info['name']:
                    admin.admin_login()
                else:
                    func(*args, **kwargs)
            # elif user_type == 'teacher':
            #     if not teacher.teacher_info['']


def get_all_obj(path):
    obj_path = path
    if os.path.exists(obj_path):
        obj_list = os.listdir(obj_path)
        return obj_list
    else:
        return None