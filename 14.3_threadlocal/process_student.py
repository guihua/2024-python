class Student(object):
    # 绑定属性, 可以通过实例直接访问
    def __init__(self, name):
        self.name = name

def do_subtask_1(std):
    print('do_subtask_1')

def do_subtask_2(std):
    print('do_subtask_2')

def process_student(name):
    # 绑定Student对象，每个Student对象都拥有各自的name和score
    std = Student(name)
    # std是局部变量，但是每个函数都要用它，因此必须传进去
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)