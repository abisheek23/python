'single inheritence'
# class synnefo:
#     def __init__(s):
#         print("register")
#     def python(s):
       
#         print('python in syn')
#     def php(self):
#         print('php')
# class novavi(synnefo):
#     def dm(s):
#         print('dm')
#     def web_dev(s):
#         print('web_dev')
# manu=synnefo()
# manu.python()

# sanu=novavi()
# sanu.web_dev()
# sanu.php

"multiple inheritence"

# class synnefo:
#     def __init__(s):
#         print("register")
#     def python(s):
       
#         print('python in syn')
#     def php(self):
#         print('php')
# class novavi():
#     def dm(s):
#         print('dm')
#     def web_dev(s):
#         print('web_dev')

# class std(synnefo,novavi):
#     def reg(self):
#         print("std reg")
# manu=synnefo()
# manu.python()

# sanu=novavi()
# sanu.web_dev()

# anu=std()
# anu.reg()
# anu.php()
# anu.python()

"multilevel inheritence"
# class colleg:
#     def _admition(self):
#         print("admition")
#     def course(self):
#         print("course")

# class class_room(colleg):
#     def student(self):
#         print("student")
# class std(class_room):
#     def reg(self):
#         print("reg")
# manu=std()
# manu.reg()
# manu._admition()

"hybrid inheriten"
class a():
    def a1(s):
        print('a1')
class b():
    def b1(s):
        print("b1")
class c(a,b):
    def c1(s):
        print("c1")
class f():
    def d1():
        print("d1")
class d(b,f):
    def f1():
        print("f1")
class e(c,d):
    def e1():
        print("e 1")