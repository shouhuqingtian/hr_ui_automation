# -*- coding: utf-8 -*-
# @Time    : 2024/9/4
# @Author  : Bin
# @Software: PyCharm
# @File    : uplode_file.py

import tkinter as tk
from tkinter import filedialog, messagebox

# 创建主窗口
root = tk.Tk()
root.title("File and Folder Uploader with Menu")
root.geometry("800x400")

# 文件路径显示的变量
path_var = tk.StringVar()


def upload_file_or_folder():
    root.withdraw()  # 隐藏主窗口

    # 让用户选择文件或文件夹
    path = filedialog.askopenfilename()  # 默认选择文件
    if not path:
        path = filedialog.askdirectory()  # 如果没有选择文件，则选择文件夹

    if path:
        messagebox.showinfo("Success", f"Selected Path: {path}")
    else:
        messagebox.showwarning("No Selection", "You did not select any file or folder.")


# 退出功能
def exit_app():
    root.quit()


# 关于功能
def show_about():
    messagebox.showinfo("About", "This is a sample file and folder uploader using Tkinter.")


# 创建菜单栏
menu_bar = tk.Menu(root)

# 创建"文件"菜单
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Upload", command=upload_file_or_folder)  # 上传按钮
file_menu.add_separator()  # 分割线
file_menu.add_command(label="Exit", command=exit_app)  # 退出按钮
menu_bar.add_cascade(label="File", menu=file_menu)

# 创建"帮助"菜单
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# 将菜单栏添加到窗口
root.config(menu=menu_bar)

# 上传按钮
upload_button = tk.Button(root, text="Upload File or Folder", command=upload_file_or_folder)
upload_button.pack(pady=20)

# 显示路径的标签
path_label = tk.Label(root, textvariable=path_var, wraplength=300)
path_label.pack(pady=10)

# 运行主循环
root.mainloop()
