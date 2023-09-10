import tkinter as tk

class Mybutton(tk.Button):
    default_color1 = "#e7efec"
    default_color2 = "#c8ddd6"
    interactive_color = "#9ed5c2"
    __default_height = 2
    __default_width = 7
    __default_relief = tk.GROOVE
    __default_bd = 3
    def __init__(self, master, color="color1", **kwargs):
        tk.Button.__init__(self, master=master)
        if color == "color2":
            self.color = self.default_color2
        else:
            self.color = self.default_color1

        self.configure( bg = self.color,
                        activebackground = self.color,
                        height = self.__default_height,
                        width = self.__default_width,
                        relief = self.__default_relief,
                        bd = self.__default_bd,)
        
        self.config(**kwargs)
        self.bind("<Enter>", self.mouse_above)
        self.bind("<Leave>", self.mouse_leave)
    
    # have *arg in function for <Enter> and <Leave>
    def mouse_above(self, e):
        self['bg'] = self.interactive_color
    
    def mouse_leave(self, e):
        self['bg'] = self.color