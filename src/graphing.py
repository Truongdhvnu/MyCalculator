import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from mybutton import Mybutton
import tkinter.font as font

class Graphing():
    def __init__(self, parent):
        #graph part
        self.figure = Figure()
        self.axes = self.figure.add_subplot(1, 1, 1)
        self.axes.grid(True)
        self.canvas = FigureCanvasTkAgg(self.figure, master=parent)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas.mpl_connect('button_press_event', self.press)
        self.canvas.mpl_connect('button_release_event', self.release)
        self.canvas.mpl_connect('scroll_event', self.zoom)
        self.func = ''

        #input part
        input_frame = tk.Frame(parent, bg=Mybutton.default_color2)
        input_frame.pack(expand=True, fill=tk.BOTH)
        tk.Label(input_frame, text="f(x) = ", bg=Mybutton.default_color2).pack(side='left', padx=7)
        self.entry_width = 40
        self.entry = tk.Entry(input_frame, width=self.entry_width, bd=3)
        self.entry.pack(side='left')
        self.entry.bind('<Key>', self.try_to_graphing)

        #init button
        button_name_list = ['x','^','( )',' + ','7','8','9',' - ','4','5','6',' x ','1','2','3',' / ','Delete','0','.','Enter']
        i = 1
        while(i < len(button_name_list)):
            new_frame = tk.Frame(parent)
            new_frame.pack(expand=True, fill="both")           
            for i in range(i, i+4):  
                #displays button
                button_font = font.Font(family='Segoe UI', size=10, weight='bold')
                button = Mybutton(new_frame, text=button_name_list[i-1], font=button_font)
                button.pack(expand=True, fill="both", side='left')    
            i += 1
        
    def try_to_graphing(self, event):
        if event.keysym == 'Delete' or event.keysym == 'BackSpace':
            self.func = self.func[:-1]
        elif event.keysym == 'Enter':
            pass
        else:
            self.func = self.entry.get() + event.keysym
        if len(self.func) > self.entry_width:
            self.entry.config(width=len(self.func))
        self.display_func()

    def display_func(self, start=-5, end=5):
        try:
            self.axes.clear()
            x_array = np.linspace(start, end, 100)
            y_array = [float(eval(self.func.replace('^', '**').replace('x', '({})'.format(i)))) for i in x_array]
            self.axes.plot(x_array, y_array)
            self.axes.set_xlim(start, end)
            self.axes.set_ylim(min(y_array) - 2, max(y_array) + 2)
            self.axes.grid(True)
            self.canvas.draw()
        except:
            print('Error on display_func')

    def zoom(self, event):
        direction = event.button
        x_min, x_max = self.axes.get_xlim()
        try:
            self.axes.clear()
            if direction == 'up':
                self.display_func(x_min * 1.2, x_max * 1.2)
            elif direction == 'down':
                self.display_func(x_min * 0.8, x_max * 0.8)
            self.axes.grid(True)
            self.canvas.draw()
        except: #draw nothing
            print("Error on zoom")

    def press(self, event):
        self.x_start = event.xdata
        self.y_start = event.ydata

    def release(self, event):
        self.x_end = event.xdata
        self.y_end = event.ydata
        self.pan(event)

    def pan(self, event):
        try:
            moving_x = self.x_end - self.x_start
            x_min, x_max = self.axes.get_xlim()
            # print(x_min, x_max)
            self.axes.clear()   # clear before right above code line or x_min, x_max = 0, 1
            self.display_func(x_min - moving_x * 0.7, x_max - moving_x * 0.7)
            self.axes.grid(True)
            self.canvas.draw()
        except:
            print("Error on pan")

if __name__ == "__main__": 
    root = tk.Tk()
    root.title("Matplotlib Window in Tkinter")

    frame2 = Graphing(root)
    frame2.func = 'x^3 + 2*x^2 - 6*x - 1'
    frame2.display_func()
    tk.mainloop()