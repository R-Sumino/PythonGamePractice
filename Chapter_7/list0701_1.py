import tkinter
root = tkinter.Tk()
root.title("初めてのテキスト入力欄")
root.geometry("400x200")
entry = tkinter.Entry(width=20)     # 20文字分の入力欄の部品を作る
entry.place(x=10, y=10)     # 入力欄の配置
root.mainloop()
