import tkinter
root = tkinter.Tk()
root.title("初めてのボタン")
root.geometry("800x600")
button = tkinter.Button(root, text="ボタンの文字列", 
                        font=("Times New Roman", 24))   # ボタンを作る
button.place(x=200, y=100)      # ボタンの表示位置指定
root.mainloop()
