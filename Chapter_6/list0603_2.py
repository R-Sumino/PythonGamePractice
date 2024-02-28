import tkinter

def click_btn():
    button["text"] = "クリックしました"

root = tkinter.Tk()
root.title("初めてのボタン")
root.geometry("800x600")
button = tkinter.Button(root, text="クリックしてください", 
                        font=("Times New Roman", 24), command=click_btn)    # クリック時の処理追加
button.place(x=200, y=100)
root.mainloop()
