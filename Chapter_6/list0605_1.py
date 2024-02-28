import tkinter
root = tkinter.Tk()
root.title("おみくじソフト")
root.resizable(False, False)    # ウィンドウサイズを固定
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="../miko.png")
canvas.create_image(400, 300, image=gazou)
root.mainloop()
