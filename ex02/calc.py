import tkinter as tk
import tkinter.messagebox as tkm

def change_mode(text): #進数表記を変更する
    global mode
    mode = text
    

def button_click(event):
    global ch_ope
    btn = event.widget
    txt = btn["text"]
    if not str(txt) in operators: #数字の入力受付
            ch_ope = False

    if mode == "DEC": #10進数の計算
        if txt == "=":
            siki = entry.get()
            res = eval(siki)
            entry.delete(0, tk.END)
            entry.insert(tk.END, res)
        
        elif txt == "C":
            entry.delete(0, tk.END)

        elif txt == "DEC": #10進数表記にする
            change_mode(txt)   

        elif txt == "BIN": #2進数表記にする
            # 計算があれば先に計算
            siki = entry.get()
            res = eval(siki)
            entry.delete(0, tk.END)
            entry.insert(tk.END, bin(int(res))[2:])
            change_mode(txt) # モード変更

        else:
            if ch_ope == False: #前に演算子が入力されていない時
                entry.insert(tk.END, txt)
                if str(txt) in operators: #記号が入力されていたら
                    ch_ope = True 
    if mode == "BIN": #2進数の計算
        if txt == "=":
            siki = entry.get()
            for kugiri in  operators:  #演算子で分割しカンマに置き換え
                siki = siki.split(kugiri)
                siki =",".join(siki)
            siki = siki.split(",")   #各2進数抽出
            res = 0
            for si in siki:
                res += int(si, 2) #10進数に変換し演算
            entry.delete(0, tk.END)
            entry.insert(tk.END, bin(int(res))[2:])
            
            
        elif txt == "C":
            entry.delete(0, tk.END)

        elif txt == "BIN":
            change_mode(txt)
        elif txt == "DEC":
            siki = entry.get()
            for kugiri in  operators:
                siki = siki.split(kugiri)
                siki =",".join(siki)
            siki = siki.split(",")
            res = 0
            for si in siki:
                res += int(si, 2)
            entry.delete(0, tk.END)
            entry.insert(tk.END, res)
            change_mode(txt)
        
        elif txt in [0, 1, "+"]: #+か0，1の時入力
            if ch_ope == False: #前に演算子が入力されていない時
                entry.insert(tk.END, txt)
                if str(txt) in operators: #記号が入力されていたら
                    ch_ope = True

# ボタン生成の関数
def mk_button(key, r, c):
    for i in key:
        button = tk.Button(root, text=i, font=("", 30), width=4, height=2)
        button.bind("<ButtonRelease>", button_click)
        button.grid(row = r, column = c)
        c += 1
        if c%3 == 0:
            r += 1
            c = 0
    return r, c


if __name__ == "__main__":
    mode = "DEC" #n進数判定
    ch_ope = False #数字以外の入力識別
    operators = ["+", "-","*", "/", "C", "=", "DEC","BIN"]

    root = tk.Tk()
    root.title("tk")
    root.geometry("280x750")
    entry = tk.Entry(root, justify="right", width=10, font=("",40))
    entry.grid(columnspan=3)

    #ボタンの実装
    r, c = 1, 0
    r, c = mk_button(range(9, -1, -1), r, c)
    r, c = mk_button(operators, r, c)

    root.mainloop()

