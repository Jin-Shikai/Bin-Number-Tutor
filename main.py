import tkinter as tk

WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 600
WINDOW_BG_COLOR = "AliceBlue"

BUTTON_WIDTH = 10
BUTTON_HEIGHT = 5
BUTTON_PAD_X = 20
BUTTON_PAD_Y = 30
BUTTON_0_COLOR = "LightCyan"
BUTTON_1_COLOR = "Salmon"
BUTTON_ACTIVE_COLOR = "PeachPuff"
BUTTON_ACTIVE_TEXT = "white"

RES_PAD_X = 20
RES_PAD_Y = 20
RES_WIDTH = 5
RES_HEIGHT = 3


class DigitBtn(tk.Button):
    def __init__(self, bit_num, btn_list, lb):

        def cal_res():
            res = 0
            for btn in btn_list:
                res += btn.val * pow(2, btn.bit_n)
            return res

        def btn_onclick():
            if self.cget("background") == BUTTON_0_COLOR:
                self.configure(background=BUTTON_1_COLOR)
                self.configure(text=1)
                self.val = 1
            else:
                self.configure(background=BUTTON_0_COLOR)
                self.configure(text=0)
                self.val = 0
            lb["text"] = cal_res()

        super().__init__(
            text=0,
            font=("Arial", 20),
            command=btn_onclick,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_0_COLOR,
            activebackground=BUTTON_ACTIVE_COLOR,
            activeforeground=BUTTON_ACTIVE_TEXT,
            cursor="hand2"
        )
        self.bit_n = bit_num
        self.val = 0
        self.pack(padx=BUTTON_PAD_X, pady=BUTTON_PAD_Y, side=tk.RIGHT)
        btn_list.append(self)


class BinNum(tk.Tk):
    global_bit = 0
    global_btn_list = []

    def __init__(self):
        super().__init__()
        self.title("Bin Number Tutor")  # 窗口名
        self.geometry(str(WINDOW_WIDTH) + 'x' +
                      str(WINDOW_HEIGHT) + '+300+150')
        # 窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        self["bg"] = WINDOW_BG_COLOR

        lb = self.add_res()

        self.add_button(lb)
        self.add_button(lb)
        self.add_button(lb)
        self.add_button(lb)

    def add_button(self, lb):
        DigitBtn(self.global_bit, self.global_btn_list, lb)
        self.global_bit += 1

    def add_res(self):
        res_label = tk.Label(text=0, font=("Arial", 30),
                             width=RES_WIDTH, height=RES_HEIGHT, relief=tk.SOLID)
        res_label.pack(padx=RES_PAD_X, pady=RES_PAD_Y, side=tk.RIGHT)
        equal_label = tk.Label(text="=", font=(
            "Arial", 30), width=RES_WIDTH, height=RES_HEIGHT, bg=WINDOW_BG_COLOR)
        equal_label.pack(padx=RES_PAD_X, pady=RES_PAD_Y, side=tk.RIGHT)
        return res_label


if __name__ == "__main__":
    app = BinNum()
    app.mainloop()
