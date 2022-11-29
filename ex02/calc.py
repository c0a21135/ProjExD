import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("tk")
root.geometry("500x1000")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    if not txt == "=":
        entry.insert(tk.END, txt)
    else:
        siki = entry.get()
        res = eval(siki)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)

entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(columnspan=3)


#数字ボタンの実装

r, c = 4, 0
for i in range(9, -1, -1):
    button = tk.Button(root, text=i, font=("", 30), width=4, height=2)
    button.bind("<ButtonRelease>", button_click)
    button.grid(row = r, column = c)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0



operators = ["+", "-","*", "/", "C", "="]
for ope in operators:
    button = tk.Button(root, text=ope, font=("", 30), width=4, height=2)
    button.bind("<ButtonRelease>", button_click)
    button.grid(row=r, column=c)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

root.mainloop()

