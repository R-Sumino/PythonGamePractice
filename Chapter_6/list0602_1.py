import tkinter
root = tkinter.Tk()
root.title("初めてのラベル")
root.geometry("800x600")
label = tkinter.Label(root, text="ラベルの文字列", 
                      font=("System", 24))     # ウィンドウに文字を出力
label.place(x=200, y=100)       # 文字の表示位置指定
root.mainloop()
