import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("tk")
root.geometry("500x1000")

mode = "DEC" #n進数判定
ch_ope = False #数字以外の入力識別
operators = ["+", "-","*", "/", "C", "=", "DEC","BIN"]
def button_click(event):
    global ch_ope, mode
    btn = event.widget
    txt = btn["text"]

    if not str(txt) in operators: #数字の入力受付
        ch_ope = False

    if txt == "=":
        siki = entry.get()
        res = eval(siki)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
    
    elif txt == "C":
        entry.delete(0, tk.END)


    else:
        if ch_ope == False:
            entry.insert(tk.END, txt)
            if str(txt) in operators: #記号の入力判定
                ch_ope = True 
    


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




for ope in operators:
    button = tk.Button(root, text=ope, font=("", 30), width=4, height=2)
    button.bind("<ButtonRelease>", button_click)
    button.grid(row=r, column=c)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0


root.mainloop()

