import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    # tkm.showwarning("警告", "ボタン押したらあかん言うたやろ")
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]ボタンが押されました")


root = tk.Tk()
root.title("おためし")
root.geometry("500x200")

label = tk.Label(root,
                text="らべると書いてみた件",
                font=("", 20)
                )
label.pack()

button = tk.Button(root, text="押すな")
button.bind("<1>", button_click)
button.pack()

# tk.Button(root, text="押すな", command=button_click).pack()


entry = tk.Entry(width=30)
entry.insert(tk.END, "fugapiyo")
entry.pack()



root.mainloop()

