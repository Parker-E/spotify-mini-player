import tkinter as tk
import math


# class VSlider(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         self.width = 100
#         self.height = 10
#         self.x = 50
#         self.y = 5
#         self.canvWidth = 12
#         self.canvHeight = 12
#         self._focus = False
#         # vslider.bind("<Button-1>", callback_1)
#         # vslider.bind("<B1-Motion>", callback_2)




#     def separation(self, x_now, y_now, x_dot, y_dot):
#         sum_squares = (x_now - x_dot)**2 + (y_now - y_dot)**2
#         distance = int(math.sqrt(sum_squares))
#         return(distance)

#     def dyn_slider(self, xn, yn, slide_val, kula, tagn):
#         self.delete(tagn)
#         self.create_line(xn, yn, xn, slide_val, fill=kula, width=4, tag=tagn)
#         self.create_rectangle(xn - 5, slide_val - 3, xn + 5, slide_val + 3, fill=kula, tag=tagn)
#         self.create_text(xn + 15, slide_val, text=str(slide_val), font=('verdana', 6), tag=tagn)

#     def canv_slider(self, xn, yn, length, kula):
#         y_top = yn - length
#         self.create_line(xn, yn, xn, y_top, fill="gainsboro", width=6)
#         self.create_rectangle(xn - 5, yn - 3, xn + 5, yn + 3, fill=kula, tag="knob_active")
#         self.create_text(xn, yn + 10, text='zero', font=('verdana', 8))
#         self.create_text(xn, y_top - 10, text='max', font=('verdana', 8))

#     def callback_1(self, event):
#         d1 = self.separation(event.x, event.y, self.x)
#         if d1 <= 5:
#             self._focus = True

#     def callback_2(self, event):
#         global length_1
#         global x_1
#         global focus_flag
#         global slide_1
#         pos_x = event.x
#         slide_val = event.y

#         if focus_flag == 1 and slide_val <= y_1 and slide_val >= y_1 - length_1 and pos_x <= x_1 + 10 and pos_x >= x_1 - 10:
#             dyn_slider(x_1, y_1, slide_val, "red", "slide_red")
#             slide_1 = slide_val



# # canv_slider(x_1, y_1, length_1, "red")























