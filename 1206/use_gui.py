# tkinter 是Python的标准GUI库，使用Tkinter可以快速简单地创建GUI应用程序
# Tkinter本身并没有提供强大的GUI控件，需要引入其他的库才能使用更丰富的GUI控件，例如：Tkinter、wxPython、PyQt、PyGTK等
# 1.wxPython是一个开源的Python GUI工具包，使用wxPython可以快速简单地创建GUI应用程序
# 2.PyQt是一个开源的Python GUI工具包，使用PyQt可以快速简单地创建GUI应用程序
# 3.PyGTK是一个开源的Python GUI工具包，使用PyGTK可以快速简单地创建GUI应用程序
#
# Tkinter和wxPython都是跨平台的GUI工具包，使用Tkinter和wxPython可以快速简单地创建GUI应用程序
# Tkinter和wxPython都是开源的，使用Tkinter和wxPython可以免费使用
# Tkinter和wxPython都是Python的标准GUI库，使用Tkinter可以快速简单地创建GUI应用程序
# Tkinter和wxPython都是跨平台的GUI工具包，使用Tkinter和wxPython可以快速简单地创建GUI应用程序

# 编写GUI程序的步骤：
# 1. 导入Tkinter模块
# 2. 创建顶层窗口对象并用它来承载整个GUI应用程序
# 3. 在顶层窗口对象上添加GUI组件
# 4. 编写GUI组件的事件处理代码
# 5. 进入消息循环
from tkinter import *
import tkinter.messagebox as messagebox

# 定义窗口类，从Frame派生，并附带一个标准的构造函数
# 该类负责创建一个GUI窗口，提供控件和事件处理回调函数，并负责布局这些控件
# 该类的实例是一个窗口对象，可以调用其pack()方法显示窗口，并调用其mainloop()方法进入消息循环，等待用户输入
class Application(Frame):
    # 构造函数，创建一个Frame并添加控件，并将其放置到父窗口中
    def __init__(self, master=None):
        # Frame.__init__(self, master)表示调用父类的构造函数，即Frame的构造函数，即创建一个Frame对象
        Frame.__init__(self, master)
        # pack()方法将Frame放置到父窗口中，即创建一个窗口对象
        self.pack()
        # 创建控件，并将其放置到窗口中
        self.createWidgets()

    # 创建控件，并将其放置到窗口中
    # 控件是GUI的基础，控件可以是文本框、按钮、列表框、单选框、复选框等
    # 控件的事件处理函数是GUI的核心，事件处理函数负责处理控件的事件，例如按钮点击事件、文本框输入事件等
    # 事件处理函数可以通过控件的command属性绑定到控件上，也可以通过控件的bind()方法绑定到控件上
    # 事件处理函数可以通过控件的config()方法修改控件的属性，例如控件的文本、背景色、前景色等
    def createWidgets(self):
        # 创建一个标签控件，显示'Hello, world!'
        # 标签控件是一个静态文本控件，用于显示文本或图像
        # 标签控件的text属性用于设置标签的文本，pack()方法将标签控件放置到窗口中
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()

        # 创建一个标签控件，显示'Name:'
        # 标签控件是一个静态文本控件，用于显示文本或图像
        # 标签控件的text属性用于设置标签的文本，pack()方法将标签控件放置到窗口中
        self.nameLabel = Label(self, text='Name:')
        self.nameInput = Entry(self)
        self.nameInput.pack()
        # 创建一个按钮控件，用于显示'Hello, xxx!'
        # 按钮控件是一个交互式控件，用于响应用户的操作
        # 按钮控件的text属性用于设置按钮的文本，command属性用于设置按钮的事件处理函数，pack()方法将按钮控件放置到窗口中
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

        # 创建一个按钮控件，用于退出程序
        # 按钮控件是一个交互式控件，用于响应用户的操作
        # 按钮控件的text属性用于设置按钮的文本，command属性用于设置按钮的事件处理函数，pack()方法将按钮控件放置到窗口中
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

# 主窗口，创建Application对象，即创建一个窗口对象
app = Application()
# 设置窗口标题
app.master.title('The first GUI')
# 主消息循环
# mainloop()方法是Frame的方法，用于进入消息循环，等待用户输入
app.mainloop()