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
            #移動先が床の場合は座標の変更と画像の差し替え
            if maze_list[mx][my-1] == 0:
                my -= 1
                image = tk.PhotoImage(file="6.png")
            #移動先が壁の場合は座標変更せずに画像の差し替えのみ
            else:
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
    # canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)

def ch_game_flag(event): #ゲームの進行を管理する関数
    global game_flag, key
    key = event.keysym
    if game_flag == False and key == "s":
        game_flag = True
    if key == "f":
        game_flag = False


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

    root.mainloop()