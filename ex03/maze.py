import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    
def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my, cx, cy
    if key == "Up":
        if maze_list[mx][my-1] == 0: my -= 1
    if key == "Down":
        if maze_list[mx][my+1] == 0: my += 1
    if key == "Left":
        if maze_list[mx-1][my] == 0: mx -= 1
    if key == "Right":
        if maze_list[mx+1][my] == 0: mx += 1
    cx, cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(width=1500, height=900, bg="black")
    image = tk.PhotoImage(file="8.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.pack()
    maze_list = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_list)
    canvas.create_image(cx, cy, image=image, tag="kokaton")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.after(100, main_proc)

    root.mainloop()