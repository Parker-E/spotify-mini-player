# tyvm to http://samclane.github.io/Gradient-Scale-Python/

import tkinter as tk


class VSlider(tk.Canvas):
    def __init__(self, master, val=50, variable=None, width=200, height=6, from_=0, to_=100, handle=None, command=None, **kwargs):
        tk.Canvas.__init__(self, master, width=width, height=height, **kwargs)
        self._value = val
        self._max = to_
        self._min = from_
        self._range = self._max - self._min
        self.command = command
        if variable is not None:
            try:
                val = int(variable.get())
            except Exception as e:
                print(e)
        else:
            self._value = tk.IntVar(self)
        val = max(min(self._max, val), self._min)
        self._value.set(val)
        self._value.trace('w', self._updateVal)

        self.bind('<Configure>', lambda e: self._drawSlider(val))
        self.bind("<ButtonPress-1>", self._onClick)
        self.bind('<ButtonRelease-1>', self._onRelease)
        self.bind("<B1-Motion>", self._onMove)

    def _drawSlider(self, val):
        self.delete("trough")
        self.delete("handle")
        width = self.winfo_width()
        height = self.winfo_height()

        # draw trough
        self.create_line(0, 0, width, height, width=width, fill='red', tags='trough')
        # TODO:
        # make these ovals work to add rounded edges to the trough
        # self.create_oval(0, 0, height, height, fill='green')

        # draw handle
        x = (val - self._min) / float(self._range) * width
        self.create_line(x, 0, x, height, width=3, fill='yellow', tags='handle')

    def _onClick(self, event):
        x = event.x
        if x >= 0:
            width = self.winfo_width()
            self.coords(self.find_withtag('handle'), x, 0, x, self.winfo_height())
            self._value.set(round((float(self._range) * x) / width + self._min, 2))
            if self.command is not None:
                self.command()

    def _onRelease(self, event):
        print(self._value.get())
        if self.command is not None:
            self.command()
        pass

    def _onMove(self, event):
        if event.x >= 0:
            w = self.winfo_width()
            x = min(max(abs(event.x), 0), w)
            self.coords(self.find_withtag('handle'), x, 0, x, self.winfo_height())
            self._value.set(round((float(self._range) * x) / w + self._min, 2))

    def _updateVal(self, *args):
        val = int(self._value.get())
        val = min(max(val, self._min), self._max)
        self.set(val)
        self.event_generate("<<ValueChanged>>")

    def get(self):
        coords = self.coords('handle')
        width = self.winfo_width()
        return round(self._range * coords[0] / width, 2)

    def set(self, val):
        width = self.winfo_width()
        x = (val - self._min) / float(self._range) * width
        for s in self.find_withtag('handle'):
            self.coords(s, x, 0, x, self.winfo_height())
        self._value.set(val)


if __name__ == '__main__':
    root = tk.Tk()
    slider = VSlider(root)
    slider.pack()
    slider.mainloop()
