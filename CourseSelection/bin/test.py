# class Foo:
#     def f1(self):
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         self.f1()

# class Bar(Foo):
#     def f0(self):
#         print('BBBB')
#
# obj = Bar()
# obj.f2()


# a = int(120)
# b = str(a)
# b = b[::-1]
# res = ''
# for i in range(len(b)):
#     if b[-1] == '0':
#         break
#     else:
#         res = res+b[i]
#
#
# print(res)


# if a == res:
#     return true
# else:
#     return false



# s = input("input:")
# res = 0
# for i in range(len(s)-1):
#     if s[i]+s[i+1] == 'IV':
#         res += 4
#     elif s[i]+s[i+1] == 'IX':
#
#
# print(res)
# import re
# string = 'azyqxxd'
# pattrn = '.zyq.'
# result = re.match(pattrn, string)
# print(result)

class Foo(object):
    def get_cls_name(self):
        return self.__class__.__name__


class Bar(Foo):
    def __init__(self):
        name = self.get_cls_name()
        print(name)

    pass


b = Bar()