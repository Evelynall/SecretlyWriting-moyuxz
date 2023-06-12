from tkinter import *
import tkinter as tk

# 统计字数的函数
def count_chars(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    text = text.replace(" ", "")  # 移除空格
    char_count = len(text)
    return char_count

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
def MouseMove2(event):
    count_root.geometry(f'+{event.x_root - mousX }+{event.y_root - mousY}')# 副窗体移动代码
    # event.x_root 为窗体相对于屏幕左上角的X坐标
    # event.y_root 为窗体相对于屏幕左上角的Y坐标

# 检测副窗口是否存在
def is_window_open(window):
    try:
        window.state()
        return True
    except tk.TclError:
        return False

# 退出事件
def exit2(event): 
    global x1
    global y1
    x1 = count_root.winfo_x()
    y1 = count_root.winfo_y()
    count_root.destroy()  #关闭字数统计窗口

def exit(event): 
    # 先保存输入框的内容到text中
    if txt.get():
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(txt.get() + '\n')  # 获取输入框内容并写入文件
        txt.delete(0, END)  # 清空输入框
    # 获取窗口位置
    x = root.winfo_x()
    y = root.winfo_y()

    # 检测副窗口是否存在
    if is_window_open(count_root):
        exit2(event)

    # 保存配置文件
    with open('config.txt', 'w') as f:
        f.write('position: ') # 位置
        f.write(f'{x},{y}')  # 用','分割x和y坐标
        f.write('\nposition2: ') # 副窗口位置
        f.write(f'{x1},{y1}')  # 用','分割x和y坐标
        f.write('\nbackground: ') # 背景颜色
        f.write(f'{backgrounds}') # 背景颜色变量
        f.write('\nforeground: ')# 前景颜色
        f.write(f'{foreground}')
        f.write('\nexitkey: ') # 退出快捷键
        f.write(f'{exitkey}')
        f.write('\nfilename: ') # 退出快捷键
        f.write(f'{filename}')
        f.write('\nwindowsize: ') # 窗口大小
        f.write(f'{windowsize}')

    root.destroy() #关闭输入窗口


# 保存输入框内容到text中
def save_file(event):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(txt.get() + '\n')  # 获取输入框内容并写入文件
    txt.delete(0, END)  # 清空输入框
    count_label['text'] = f'{count_chars(filename)}' 


# 字数统计窗口设置
count_root = Tk()
count_root.geometry('60x20')   
count_root.overrideredirect(True)  # 无标题栏窗体
count_root.wm_attributes("-topmost", 1)  # 使窗口置顶

# 输入窗口设置
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
    # 读取第二行前十一个字符（即position2: ）
    a = f.readline(11) 
    # 读取第二行剩余字符 用','分割读取坐标
    x1, y1 = f.readline().split(',')  
    x1 = int(x1) # 将坐标转为整数
    y1 = int(y1)
    count_root.geometry(f'+{x1}+{y1}') # 副窗口
    # 读取第三行前12个字符（background: ）
    a = f.readline(12) 
    # 设置背景颜色（后半段为去除换行符）
    backgrounds = f.readline().replace('\r','').replace('\n','') 
    # 设置前景(字体)颜色
    a = f.readline(12)
    foreground = f.readline().replace('\r','').replace('\n','')
    # 读取第四行前9个字符（exitkey: ）
    a = f.readline(9) 
    # 设置退出快捷键
    exitkey = f.readline().replace('\r','').replace('\n','')
    # 读取第五行前10个字符（filename: ）
    a = f.readline(10) 
    # 设置文件位置
    filename = f.readline().replace('\r','').replace('\n','')
    # 读取第六行前12个字符（windowsize: ）
    a = f.readline(12) 
    # 设置窗口大小
    windowsize = f.readline().replace('\r','').replace('\n','')
    root.geometry(windowsize)

root.config(bg=backgrounds)
# 设置输入框
txt = Entry(root, bg=backgrounds, bd=0, fg=foreground)
txt.grid(column=1, row=0)
txt.focus()

# Label显示字数
count_label = Label(count_root,bg=backgrounds, bd=0, fg=foreground, text=f' {0}')  
count_label.pack()   
count_label.pack(fill=tk.BOTH, expand=True)

# 初始化时更新 
count_label['text'] = f' {count_chars(filename)}'  

# 绑定键入事件  
txt.bind('<Key>', lambda event: update_count())  
    
# 实时更新字数显示的函数  
def update_count(): 
    count_label['text'] = f'{count_chars(filename)}' 

# 设置窗口大小变化事件
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.bind('<Configure>', lambda event: txt.config(width=event.width-10))

root.bind("<Button-1>",MouseDown)  # 按下鼠标左键绑定MouseDown函数
root.bind("<B1-Motion>",MouseMove)  # 鼠标左键按住拖曳事件,3个函数都不要忘记函数写参数
root.bind("<Double-Button-1>",exit)  # 双击鼠标左键，关闭窗体
count_root.bind("<Button-1>",MouseDown)  # 按下鼠标左键绑定MouseDown函数
count_root.bind("<B1-Motion>",MouseMove2)  # 鼠标左键按住拖曳事件,3个函数都不要忘记函数写参数
count_root.bind("<Double-Button-1>",exit2)  # 双击鼠标左键，关闭窗体
txt.bind('<Return>', save_file)   # 按下回车将文本保存至text
root.bind(exitkey, exit) # 按下自定义退出快捷键触发退出事件

root.mainloop()