from graphing import Graphing
from standard import Standard
import tkinter as tk
from tkinter import ttk

''' Just to demonstate that this work for importing between these relative file and running "int main()" func of each files
import os
import sys
current_dir = os.path.dirname(__file__)
code_path = os.path.join(current_dir, '..', "tests")
sys.path.append(code_path)
from testunit import test
'''

class MyApp:
    def __init__(self, root:tk.Tk):
        self.root = root
        self.root.title("My Calculator")
        self.root.attributes("-alpha", 0.9)    
        self.root.geometry('405x702')
        self.create_tabs()
    
    def create_tabs(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)
        
        standard_frame = ttk.Frame(self.notebook)
        graphing_frame = ttk.Frame(self.notebook)
        
        standard = Standard(standard_frame)    
        graphing = Graphing(graphing_frame)

        self.notebook.add(standard_frame, text="Standard")
        self.notebook.add(graphing_frame, text="Graphing")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

## can Standard and Graphing class can iherit tk.Frame and call standard_frame = Stardard(self.notebook) only?
'''
The primary version, i create 2 new frame that inside an other root_frame(this frame in right inside root)
Then, i create a Standard and Graphing for each frames so the root_frame is like the notebook above
But, i have to manually create menu and manipulate the display on-off of each frame by using two functions: 
    + pack() : turn-on display of an frame
    + pack_forget() : turn-off display of an frame
So, we have 2 tk.Button that bind with 2 switching display functions 
'''