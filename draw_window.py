import tkinter as tk
from PIL import Image, ImageTk
import mss
from functools import partial

class color:
    color = ''
    def set_red():
        color.color = "red"
    def set_black():
        color.color = "black"
    def set_blue():
        color.color = "blue"
    def set_white():
        color.color = "white"
    def set_green():
        color.color = "green"

def create_left_board(self):
    draw_btn = tk.Button(self, image=self.pen_img, borderwidth=0, highlightthickness=0, bg="black", relief="flat", command=self.penDraw)
    draw_btn.image = self.pen_img
    draw_btn.pack(pady=5)
    draw_btn = tk.Button(self, image=self.red_img, borderwidth=0, highlightthickness=0, bg="black", relief="flat", command=color.set_red)
    draw_btn.image_red = self.red_img
    draw_btn.pack(pady=5)
    draw_btn = tk.Button(self, image=self.blue_img, borderwidth=0, highlightthickness=0, bg="black", relief="flat", command=color.set_blue)
    draw_btn.image_blue = self.blue_img
    draw_btn.pack(pady=5)
    draw_btn = tk.Button(self, image=self.green_img, borderwidth=0, highlightthickness=0, bg="black", relief="flat", command=color.set_green)
    draw_btn.image_green = self.green_img
    draw_btn.pack(pady=5)
    draw_btn = tk.Button(self, image=self.black_img, borderwidth=0, highlightthickness=0, bg="black", relief="flat", command=color.set_black)
    draw_btn.image_black = self.black_img
    draw_btn.pack(pady=5)
    draw_btn = tk.Button(self, image=self.white_img, borderwidth=0, highlightthickness=0, bg="black", relief="flat", command=color.set_white)
    draw_btn.image_white = self.white_img
    draw_btn.pack(pady=5)
    draw_btn = tk.Button(self, image=self.quit_img, borderwidth=0, highlightthickness=0, bg="black", relief="flat", command=self.root.destroy)
    draw_btn.image_quit = self.quit_img
    draw_btn.pack(pady=5)

class ToolWin(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        pil_img = Image.open("assets/pen.png")
        self.pen_img = ImageTk.PhotoImage(pil_img)
        pil_img = Image.open("assets/red.png")
        self.red_img = ImageTk.PhotoImage(pil_img)
        pil_img = Image.open("assets/blue.png")
        self.blue_img = ImageTk.PhotoImage(pil_img)
        pil_img = Image.open("assets/green.png")
        self.green_img = ImageTk.PhotoImage(pil_img)
        pil_img = Image.open("assets/black.png")
        self.black_img = ImageTk.PhotoImage(pil_img)
        pil_img = Image.open("assets/white.png")
        self.white_img = ImageTk.PhotoImage(pil_img)
        pil_img = Image.open("assets/quit.png")
        self.quit_img = ImageTk.PhotoImage(pil_img)
        self.root = root
        self.resizable(False, False)
        self['background']="#000000"
        self._offsetx = 0
        self._offsety = 0
        self.wm_attributes('-topmost', 1)
        self.geometry('60x370+0+400')
        self.minsize(60, 370)
        self.maxsize(60, 370)
        self.penModeId = None
        self.penSelect = tk.BooleanVar()
        self.overrideredirect(True)
        self.bind('<ButtonPress-1>', self.clickTool)
        self.bind('<B1-Motion>', self.moveTool)
        create_left_board(self)
        
    def moveTool(self, event):
        self.geometry(f"200x200+{self.winfo_pointerx() - self._offsetx}+{self.winfo_pointery() - self._offsety}")

    def clickTool(self, event):
        self._offsetx = event.x
        self._offsety = event.y

    def penDraw(self):
        if self.penSelect == 1:
            self.penSelect = 0
        else:
            self.penSelect = 1
        if self.penSelect == 1:
            self.penModeId = fullCanvas.bind("<B1-Motion>", Draw)
        else:
            fullCanvas.unbind("<B1-Motion>")

def Draw(event):
    x, y = event.x, event.y
    fullCanvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill=color.color, outline=color.color)

with mss.mss() as sct:
    monitor = sct.monitors[0]
    sct_img = sct.grab(monitor)
    img = Image.frombytes("RGB", sct_img.size, sct_img.rgb)
color.color = "black"
root = tk.Tk()
root.state('normal')
root.attributes("-fullscreen", True)
fullCanvas = tk.Canvas(root, cursor="tcross")
background = ImageTk.PhotoImage(img)
fullCanvas.create_image(0, 0, anchor="nw", image=background)
fullCanvas.pack(fill="both", expand=True)
root.after(300, lambda: ToolWin(root))
root.mainloop()
