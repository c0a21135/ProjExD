import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("tk")
root.geometry("300x500")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]ボタンがクリックされました")

for i in range(9, -1, -1):
    button = tk.Button(root, text=9-i, font=("", 30), width=4, height=2)
    button.bind("<ButtonRelease>", button_click)
    button.grid(row = (i//3), column = (i%3))

root.mainloop()