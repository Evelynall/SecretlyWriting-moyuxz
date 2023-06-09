from tkinter import *
 
# 鼠标左键按下事件
def MouseDown(event): # 不要忘记写参数event
    global mousX  # 全局变量，鼠标在窗体内的x坐标
    global mousY  # 全局变量，鼠标在窗体内的y坐标
 
    mousX=event.x  # 获取鼠标相对于窗体左上角的X坐标
    mousY=event.y  # 获取鼠标相对于窗左上角体的Y坐标

# 鼠标按下后的移动事件
def MouseMove(event):
    root.geometry(f'+{event.x_root - mousX}+{event.y_root - mousY}') # 窗体移动代码
    # event.x_root 为窗体相对于屏幕左上角的X坐标
    # event.y_root 为窗体相对于屏幕左上角的Y坐标

# 退出事件
def exit(event): 
    # 先保存输入框的内容到text中
    if txt.get():
        with open(filename, 'a') as f:
            f.write(txt.get() + '\n')  # 获取输入框内容并写入文件
        txt.delete(0, END)  # 清空输入框
    # 获取窗口位置
    x = root.winfo_x()
    y = root.winfo_y()

    # 保存配置文件
    with open('config.txt', 'w') as f:
        f.write('position: ') # 位置
        f.write(f'{x},{y}')  # 用','分割x和y坐标
        f.write('\nbackground: ') # 背景颜色
        f.write(f'{backgrounds}') # 背景颜色变量
        f.write('\nforeground: ')# 前景颜色
        f.write(f'{foreground}')
        f.write('\nexitkey: ') # 退出快捷键
        f.write(f'{exitkey}')
        f.write('\nfilename: ') # 退出快捷键
        f.write(f'{filename}')
    root.destroy()

# 保存输入框内容到text中
def save_file(event):
    with open(filename, 'a') as f:
        f.write(txt.get() + '\n')  # 获取输入框内容并写入文件
    txt.delete(0, END)  # 清空输入框
 
root=Tk()
root.geometry('300x20')
root.overrideredirect(True)  # 无标题栏窗体
root.wm_attributes("-topmost", 1)  # 使窗口置顶

# 窗口打开事件（读取配置文件）
with open('config.txt') as f:
    # 读取第一行前十个字符（即position: ）
    a = f.readline(10) 
    # 读取第一行剩余字符 用','分割读取坐标
    x, y = f.readline().split(',')  
    x = int(x) # 将坐标转为整数
    y = int(y)
    root.geometry(f'+{x}+{y}')  # 设置窗口位置
    # 读取第二行前12个字符（background: ）
    a = f.readline(12) 
    # 设置背景颜色（后半段为去除换行符）
    backgrounds = f.readline().replace('\r','').replace('\n','') 
    # 设置前景(字体)颜色（后半段为去除换行符）
    a = f.readline(12)
    foreground = f.readline().replace('\r','').replace('\n','')
    # 读取第三行前9个字符（exitkey: ）
    a = f.readline(9) 
    # 设置退出快捷键（后半段为去除换行符）
    exitkey = f.readline().replace('\r','').replace('\n','')
    # 读取第四行前10个字符（filename: ）
    a = f.readline(10) 
    # 设置退出快捷键（后半段为去除换行符）
    filename = f.readline().replace('\r','').replace('\n','')

root.config(bg=backgrounds)
# 设置输入框
txt = Entry(root, bg=backgrounds, bd=0, fg=foreground)
txt.grid(column=1, row=0)
txt.focus()

# 设置窗口大小变化事件
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.bind('<Configure>', lambda event: txt.config(width=event.width-10))

root.bind("<Button-1>",MouseDown)  # 按下鼠标左键绑定MouseDown函数
root.bind("<B1-Motion>",MouseMove)  # 鼠标左键按住拖曳事件,3个函数都不要忘记函数写参数
root.bind("<Double-Button-1>",exit)  # 双击鼠标左键，关闭窗体
txt.bind('<Return>', save_file)   # 按下回车将文本保存至text
root.bind(exitkey, exit) # 按下自定义退出快捷键触发退出事件

root.mainloop()