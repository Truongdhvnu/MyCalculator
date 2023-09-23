import tkinter.font as font
import tkinter as tk
from mybutton import Mybutton

class Standard():
    button_color2_list = [1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 20, 24]
    button_color1_list = [9, 10, 11, 13, 14, 15, 17, 18, 19, 21, 22, 23]
    button_bold_list = [9, 10, 11, 13, 14, 15, 17, 18, 19, 21]
    button_name_list = ['%', 'CE', 'C', 'Delete', '1/x', 'x^2', 'sqrt(x)', ' / ', '7', '8', '9', ' x ',\
                        '4', '5', '6', ' - ', '1', '2', '3', ' + ', '+/-', '0', '.', '=']
    number_type_func_list = [9, 10, 11, 13, 14, 15, 17, 18, 19, 22]
    common_operator_func_list = [20, 16, 12, 8]

    ## setup command for buttons
    error_message = 'Sth wrong!'
    erorr_mode = (1)
    active_mode = (0)

    def __init__(self, parent):
        self.mode = self.active_mode
        # expression_frame : arg1 
        expression_frame = tk.Frame(parent)
        expression_frame.pack(expand=1, fill="both")
        expresion_font = font.Font(family='Segoe UI', size=16)
        self.expresion = tk.Label(expression_frame, height=1, bg='#f0f0f0', font=expresion_font, anchor='se')
        self.expresion.pack(expand=True, fill="both")
        #input : arg2
        input_frame = tk.Frame(parent)
        input_frame.pack(expand=1, fill="both")
        input_font = font.Font(family='Segoe UI', size=50)
        self.input = tk.Label(input_frame, height=1, bg='#f0f0f0', font=input_font, anchor='se')
        self.input.pack(expand=True, fill="both")
        
        i = 1
        while(i < 25):
            new_frame = tk.Frame(parent)
            new_frame.pack(expand=1, fill="both")
            
            for i in range(i, i+4):
                
                #displays button
                button_font = font.Font(family='Segoe UI', size=10)
                if i in self.button_bold_list:                           #dung self.input_str khong duoc vay tai sao cai font lai thay doi?
                    button_font['weight'] = 'bold'                  #size of button w/h base on current font so the cell will "xoc xech" neu both bold and normal
                else:
                    button_font['weight'] = 'bold'
                global button
                if i in self.button_color2_list:
                    button = Mybutton(new_frame, color="color2", text=self.button_name_list[i-1], font=button_font)
                elif i in self.button_color1_list:
                    button = Mybutton(new_frame, color="color1", text=self.button_name_list[i-1], font=button_font)
                button.pack(expand=1, fill="both", side='left')    
                
                #bind command for each button
                if i in self.number_type_func_list:
                    button['command'] = lambda num=i: self.number_type_func(num) 
                elif i==23:
                    button['command'] = self.dot_func
                elif i in self.common_operator_func_list:
                    button['command'] = lambda num=i: self.common_operator_func(num) 
                elif i==24:
                    button['command'] = self.equals_func
                elif i==21:
                    button['command'] = self.reverse_func
                elif i==5:
                    button['command'] = self.inverse_func
                elif i==6:
                    button['command'] = self.sqr_func
                elif i==7:
                    button['command'] = self.sqrt_func
                elif i==4:
                    button['command'] = self.delete_func
                elif i==3:
                    button['command'] = self.C_func
                elif i==2:
                    button['command'] = self.CE_func
            i += 1

    # support func 
    def result_toString(self, var: float|int) -> str:
        if int(var) - var == 0:
            var = int(var)
            return str(var)
        else:
            try:
                return str(var)[:20]
            except:
                return str(var)

    def number_type_func(self, i):
        if self.mode == self.active_mode:
            self.input['text'] += self.button_name_list[i-1]
    
    def dot_func(self):
        if self.mode == self.active_mode:
            if "." not in self.input['text']:
                self.input['text'] += "."
    
    def common_operator_func(self, i):
        if self.mode == self.active_mode:
            def check_exist():
                for e in [' / ', ' + ',  ' - ', ' x ']:
                    if e in self.expresion['text']:
                        return e
                return False
            if (operator := check_exist()) != False:        # have operator
                if self.input['text'] != '':                # have operator + have agr2 --> calculate the result
                    self.expresion['text'] += self.input['text']
                    try:
                        result = eval(self.expresion['text'].replace('x', '*'))
                        self.expresion['text'] = self.result_toString(result) + self.button_name_list[i-1]
                        self.input['text'] = ''
                    except:
                        self.input['text'] = self.error_message
                        self.mode = self.erorr_mode
                else:                                   # have operator + not have agr2 --> update orperator
                    self.expresion['text'] = self.expresion['text'].replace(operator, self.button_name_list[i-1])
            else:                                       # do not have operator
                if self.input['text'] != '':                 # have arg in self.input
                    self.input['text'] += self.button_name_list[i-1]
                    self.expresion['text'] = self.input['text']
                    self.input['text'] = ''
                else:
                    if self.expresion['text'] != '':
                        self.expresion['text'] += self.button_name_list[i-1]
                    elif self.expresion['text'] == '':
                        pass
        
    def equals_func(self):
        if self.mode == self.active_mode:
            total_expression = self.expresion['text'] + self.input['text']
            self.input['text'] = ''
            try:
                result = eval(total_expression.replace('x', '*'))
                self.expresion['text'] = self.result_toString(result)
            except:
                self.input['text'] = self.error_message
                self.mode = self.erorr_mode

    def reverse_func(self):
        if self.mode == self.active_mode:
            if self.input['text'] != '':                 # self.input not empty
                try:
                    result = float(eval(self.input['text'].replace('x', '*'))) * -1
                    self.input['text'] = self.result_toString(result)
                except:
                    pass
            elif self.expresion['text'] != '':           # self.input empty: if have arg in self.expresion, reverse it    
                try:
                    result = float(eval(self.expresion['text'].replace('x', '*'))) * -1
                    self.expresion['text'] = self.result_toString(result)
                except:
                    pass
            else:                                   # have no arg in self.input and no arg in self.expresion
                pass

    def inverse_func(self):
        if self.mode == self.active_mode:
            if self.input['text'] != '':                 # self.input not empty
                try:
                    print(self.input['text'])
                    result = 1/float(eval(self.input['text'].replace('x', '*')))
                    self.input['text'] = self.result_toString(result)
                except:
                    pass
            elif self.expresion['text'] != '':           # self.input empty: if have arg in self.expresion, inverse it    
                try:
                    result = 1/float(eval(self.expresion['text'].replace('x', '*')))
                    self.expresion['text'] = self.result_toString(result)
                except:
                    pass
            else:                                   # have no arg in self.input and no arg in self.expresion
                pass

    def sqr_func(self):
        if self.mode == self.active_mode:
            if self.input['text'] != '':                 # self.input not empty
                try:
                    result = float(eval(self.input['text'].replace('x', '*')))**2
                    self.input['text'] = self.result_toString(result)
                except:
                    pass
            elif self.expresion['text'] != '':           # self.input empty, have arg in self.expresion
                try:
                    result = float(eval(self.expresion['text'].replace('x', '*')))**2
                    self.expresion['text'] = self.result_toString(result)
                except:
                    pass
            else:                                   # have no arg in self.input and no arg in self.expresion
                pass

    def sqrt_func(self):
        if self.mode == self.active_mode:
            if self.input['text'] != '':                 # self.input not empty
                try:
                    result = float(eval(self.input['text'].replace('x', '*')))**0.5
                    self.input['text'] = self.result_toString(result)
                except:
                    pass
            elif self.expresion['text'] != '':           # self.input empty, have arg in self.expresion
                try:
                    result = float(eval(self.expresion['text'].replace('x', '*')))**0.5
                    self.expresion['text'] = self.result_toString(result)
                except:
                    pass
            else:                                   # have no arg in self.input and no arg in self.expresion
                pass 

    def percent_func(self):
        pass
    
    def C_func(self):
        self.input['text'] =''
        self.expresion['text'] = ''
        self.mode = self.active_mode

    def CE_func(self):
        self.input['text'] =''  
        self.mode = self.active_mode

    def delete_func(self):
        if self.mode == self.active_mode:
            self.input['text'] = self.input['text'][:len(self.input['text']) - 1]

if __name__ == '__main__':
    root = tk.Tk()
    standard = Standard(root)
    root.geometry('405x702')
    tk.mainloop()

    # self.expresion['text'] = str(4)
    # self.input['text'] = str(eval("1+2+sqrt(3)"))

    '''
    use grid can't change the size when we change the size of parent, 
    sticky: what to do if cell larger than widget
    So in this case, because all button have the same size = SIZE,
    each cell will have the same size=SIZE and grid do no allow expand as pack(), sticky.tk.NSEW is useless
    '''
    '''
    frame = tk.Frame(root)                                       # frame will auto resize according to the widgets it contains
    frame.pack(expand=1, fill="both")                            # use pack in order the widgets can change size and fill space
    button1 = Mybutton(frame, color="color1", text='click here')
    button1.pack(expand=1, fill="both", side='left')           
    # button1.grid(row=0, column=0)
    button1 = Mybutton(frame, color="color2", text='click here')
    button1.pack(expand=1, fill="both", side='right')
    # button1.grid(row=0, column=1)               
    '''

    #rowspans and columnspan seem not work (set not change size display), the width and height do this now
    # expression = tk.Label(root, text='hi', width=40, height=1, bg='yellow')
    # expression.grid(row=0, column=0, rowspan=1, columnspan=4, sticky=tk.NSEW)

    # self.input = tk.Label(root, text='ka', width=40, height=3)
    # self.input.grid(row=1, column=0, rowspan=3, columnspan=4, sticky=tk.NSEW)

    # button1 = Mybutton(root, color="color1", text='click here', bg="green")
    # button1.grid(row=4, column=0, sticky=tk.NSEW)
    # button1 = Mybutton(root, color="color2", text='click here', bg="blue")
    # button1.grid(row=4, column=1, sticky=tk.NSEW)