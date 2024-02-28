import tkinter
root = tkinter.Tk()
root.title("初めてのキャンバス")
canvas = tkinter.Canvas(root, width=400, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="iroha.png")    # 画像を読み込み
canvas.create_image(200, 300, image=gazou)      # 画像出力
root.mainloop()
