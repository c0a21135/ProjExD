import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    
def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my, cx, cy, image
    if game_flag == True: #ゲーム実施中のみ移動ができる
        if key == "Up":
            if maze_list[mx][my-1] == 0: #移動先が床の場合は座標の変更と画像の差し替え
                my -= 1
                image = tk.PhotoImage(file="6.png")
            else:                        #移動先が壁の場合は座標変更せずに画像の差し替えのみ
                image = tk.PhotoImage(file="8.png")

        if key == "Down":
            if maze_list[mx][my+1] == 0: 
                my += 1
                image = tk.PhotoImage(file="3.png")
            else:
                image = tk.PhotoImage(file="8.png")

        if key == "Left":
            if maze_list[mx-1][my] == 0:
                mx -= 1
                image = tk.PhotoImage(file="5.png")
            else:
                image = tk.PhotoImage(file="8.png")

        if key == "Right":
            if maze_list[mx+1][my] == 0:
                mx += 1
                image = tk.PhotoImage(file="2.png")
            else: 
                image = tk.PhotoImage(file="8.png")

    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=image, tag="kokaton")
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)

def ch_game_flag(event): #ゲームの進行を管理する関数
    global game_flag, key
    key = event.keysym
    # ゲームの開始
    if game_flag == False and key == "s":
        game_flag = True
        time_count() #タイマーの開始
    # ゲームの一時停止
    if key == "f":
        game_flag = False
        time_count() #タイマーの停止
    # ゲームの初期化
    if key == "r":
        game_flag = False
        init()

def time_count(): #時間の計測と表示
    global sec, ms, jid
    if game_flag == True:
        ms += 1
        if ms == 10:
            ms = 0
            sec += 1
        jid = root.after(100, time_count)
    if game_flag == False:
        root.after_cancel(jid)
    label["text"] = f"{sec}.{ms}"
    label.pack()

def init():
    global mx, my, sec, ms, image
    sec, ms = 0, 0
    image = tk.PhotoImage(file="0.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.pack()
    mm.show_maze(canvas, maze_list)
    canvas.create_image(cx, cy, image=image, tag="kokaton")
    time_count()

if __name__ == "__main__":
    game_flag = False
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(width=1500, height=900, bg="black")
    image = tk.PhotoImage(file="0.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.pack()
    maze_list = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_list)
    canvas.create_image(cx, cy, image=image, tag="kokaton")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyPress>", ch_game_flag)
    root.bind("<KeyRelease>", key_up)
    root.after(100, main_proc)
    label = tk.Label(root, font=("", 80))
    sec, ms = 0, 0
    label["text"] = f"{sec}.{ms}"
    label.pack()

    root.mainloop()