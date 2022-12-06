import tkinter as tk

def key_down(event):
    global key
    key = event.keysym


root = tk.Tk()
root.title("迷えるこうかとん")
canvas = tk.Canvas(width=1500, height=900, bg="black")
image = tk.PhotoImage(file="8.png")
cx = 300
cy = 400
canvas.create_image(cx, cy, image=image)
canvas.pack()
key = ""
root.bind("<KeyPress>", key_down)

root.mainloop()