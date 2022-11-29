import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("tk")
root.geometry("300x500")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]ボタンがクリックされました")

entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row = 0, column = 0, columnspan=3)

for i in range(9, -1, -1):
    button = tk.Button(root, text=9-i, font=("", 30), width=4, height=2)
    button.bind("<ButtonRelease>", button_click)
    button.grid(row = (i//3)+1, column = (i%3))

r, c = 4, 1
operators = ["+", "="]
for ope in operators:
    button = tk.Button(root, text=ope, font=("", 30), width=4, height=2)
    button.bind("<ButtonRelease>", button_click)
    button.grid(row=r, column=c)
    c+=1

root.mainloop()

