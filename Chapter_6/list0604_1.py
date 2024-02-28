import tkinter
root = tkinter.Tk()
root.title("初めてのキャンバス")
canvas = tkinter.Canvas(root, width=400, height=600,
                        bg="skyblue")       # キャンバスを作成
canvas.pack()       # pack メソッドを使うことでgeometoryで指定しなくてよい
root.mainloop()
