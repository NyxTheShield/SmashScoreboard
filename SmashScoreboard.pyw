from tkinter import *    
from tkinter import ttk  
from tkinter import filedialog
from tkinter import messagebox
import re
import base64

photo = "R0lGODlhkAFkAPcAAMnJyVRUVIiIiI+Pj4p+fY6BgVZWVq6lpdra2vr6+tHR0aCWlXR0dFZDQrKqqiEhISUNDc3NzZSKiTExMSEJCJGRkfz8/EYyMUk1NBIAAOLf3+7u7sLCwjgiIcbGxsG6uj4pKBEREYWFhZ+fn97e3mlpaeTk5Hl5eeDg4Ly1tU1NTcDAwIGBgWVlZeTh4T4+Pp2SkV1dXRoaGlFRUUhISPPz8+rq6tHMzHpra5qamqysrH19faWlpdXV1bi4uHp6em5ubjolJOLi4hwCAUItLE06OTQeHTk5OWZVVcTExKOZmd3Z2RwDAjchILS0tOjo6JeXlx0dHVE+PW1eXaGhoXFxcYqKil9NTGNSUcrExLKysjMdHAsLCxgAAJycnPHu7nNkY/Ly8piYmP7+/i0tLampqQICAujl5VhYWEFBQaSamioTEpCEhKOjo2NjY6qqqltbW7CwsO3r6oZ6eWpaWTIcGy8YGCwVFB8GBaednCgRECkpKTEaGe7s7Ozs7H5wcCYmJt3c276+vs/JyTwmJZ+UlDIbGjkkIyAIBycQD1hFRC4XFpeMizYgHz0oJzAZGEdHRywWFdnV1Z6Ukzw8PEQwL/X19fTy8h4JCfPx8TAaGGBOTSkUFI2AgIt/fkEsK2VUUy8YF4h7eyUREUArKiwXFw0AAJSIhyQMC11LSxQUFKqgoB4FBB8HBl1MSykSEVtJSCINDW9gXxwFBL29vdnZ2RoEBBwGBSILChwHBpOTk2BgYBgDA+fn59fX1/f397a2tpWVlfDw8CAHBisUE+bm5uHe3uPg4Ly8vLe3t/n5+ZSUlPj4+GFQTywUE2FhYZKSktjY2EMvLvb29tbW1ioSEbq6uvv7+/f29mhYV6KYl/Hx8SMLCi0WFfn4+FpIR+Pf3/r5+WdXVh8ICIl8fPj393VnZ19QUCcPDkY4N9XQ0Eo4N+bj42tcXFNAQIN3d5uQj8a/wH9xcHdoZ+fk5Oro6KWcm/39/ZuQkGNSUmZYV7iwsOXi4hsCAQAAAP///yH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS4zLWMwMTEgNjYuMTQ1NjYxLCAyMDEyLzAyLzA2LTE0OjU2OjI3ICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ4bXAuZGlkOjcwM0VGRTE0RjMzRkU5MTE4MTE0RjFCMjdFNzU1RkZEIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkVDRjlBM0YwM0ZGMzExRTk5OENBQjZEQTA0OUJDRkE4IiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkVDRjlBM0VGM0ZGMzExRTk5OENBQjZEQTA0OUJDRkE4IiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDUzYgKFdpbmRvd3MpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6NzkzRUZFMTRGMzNGRTkxMTgxMTRGMUIyN0U3NTVGRkQiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6NzAzRUZFMTRGMzNGRTkxMTgxMTRGMUIyN0U3NTVGRkQiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz4B//79/Pv6+fj39vX08/Lx8O/u7ezr6uno5+bl5OPi4eDf3t3c29rZ2NfW1dTT0tHQz87NzMvKycjHxsXEw8LBwL++vby7urm4t7a1tLOysbCvrq2sq6qpqKempaSjoqGgn56dnJuamZiXlpWUk5KRkI+OjYyLiomIh4aFhIOCgYB/fn18e3p5eHd2dXRzcnFwb25tbGtqaWhnZmVk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"
icon = "R0lGODlhQABAAPf/AK2lpLmxsZmOjuzq6lFCQWRTUsvFxTMhISoUFEEuLUw+PbaurjYkJC4YGKqgnywXFo6CgYJ2dqCWlTAcHOTi4SgSEjQgIOro6DMfHqienjAbGqSbmjopKCYQDzwrK5+VlScPD723t9XQ0CYPDvLx8TMgIHpsbEk2NTIdHKednS0YFy0aGkw8PEY3Nj4tLHFhYB4FBDUiIiAICM3Hx05BQR4GBUg4NjkmJl9NTSwYGEI1NSMLCjIcG9zZ2TQiItbR0FJGRkIzM0o9PNHNyygQEBAAAB8GBTgmJjwtLRwCAbSsq0xAP1VGRkUwLyoTEzEeHiUNDDgoKEQ0NCoWFjYkIzosKxwEA0Q2NjcjIi0XFykTEz4rKzQeHTYgICcREUEzMzYiIR0FBDwnJjwqKUU0MzooJ2FPTj8wLzgkIywWFTQiISQODkk6OTIdHR8HBks5ODclJTolJRoEBD8wMBgCAUEwLyILCy8bGzwpKSUODSsVFTEbGiEJCBkDAyAIB9TPz9POzufl5dLNzeTh4efl5CIKCePg4Obk46OZmeLf3zAaGSQMC/v7+/v6+iYODeLe3uTh4PX09Pn4+OXi4uPf3/r5+aKYmOjm5unn5+fk5P39/T0sLObj4+bk5PTz8y0ZGaOamaKXlyEKCUAvLzgkJNTQz+Hd3ff29kAuLero50MyMZyRkfPy8o2FheXj4rewr9rV1aSamUk7OmhXVmlaV5+VksG7tzEdHKacm4Z5eIl/flZDQi4cHKegoKGWlhwGBRwHBrKpqenn5mpdXS8aGiQNDKOamnBkYnJmZs7LyyYYGOLf3ujl5VhFRPHw8PPy8ZaKif7+/rOsqCkSEaKYl9fS0uTg4OPg30M0M3VlZUQyMfv7+qKZmaOZmOnm5u7s7NHOzpuQj56Tk8jCwUc1NEU2Nby0s9vZ2SgVFe3r6x8IB0AyMUExMMG6ucK8usS9vNPPz9jV1dvX1qSZmZySkOTi4kk8O+Xj497b2C8ZGUw7OllLSh0EAxwDAhsCAf///yH/C1hNUCBEYXRhWE1QPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS4zLWMwMTEgNjYuMTQ1NjYxLCAyMDEyLzAyLzA2LTE0OjU2OjI3ICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ1M2IChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo4OUIwQTRFNDNGRjcxMUU5OENFMTk0MTYxOUFGQjVCQyIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo4OUIwQTRFNTNGRjcxMUU5OENFMTk0MTYxOUFGQjVCQyI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjg5QjBBNEUyM0ZGNzExRTk4Q0UxOTQxNjE5QUZCNUJDIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjg5QjBBNEUzM0ZGNzExRTk4Q0UxOTQxNjE5QUZCNUJDIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+Af/+/fz7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4uHg397d3Nva2djX1tXU09LR0M/OzczLysnIx8bFxMPCwcC/vr28u7q5uLe2tbSzsrGwr66trKuqqainpqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2Mi4qJiIeGhYSDgoGAf359fHt6eXh3dnV0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUlFQT05NTEtKSUhHRkVEQ0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEg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"
swap = "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"
#=============================================
# GUI Code
#=============================================

def matches(fieldValue, acListEntry):
        pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
        return re.match(pattern, acListEntry)
    
class AutocompleteEntry(Entry):
    def __init__(self, autocompleteList, *args, **kwargs):

        # Listbox length
        if 'listboxLength' in kwargs:
            self.listboxLength = kwargs['listboxLength']
            del kwargs['listboxLength']
        else:
            self.listboxLength = 8

        # Custom matches function
        if 'matchesFunction' in kwargs:
            self.matchesFunction = kwargs['matchesFunction']
            del kwargs['matchesFunction']
        else:
            def matches(fieldValue, acListEntry):
                pattern = re.compile('.*' + re.escape(fieldValue) + '.*', re.IGNORECASE)
                return re.match(pattern, acListEntry)
                
            self.matchesFunction = matches

        
        Entry.__init__(self, *args, **kwargs)
        self.focus()

        self.autocompleteList = autocompleteList
        
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Return>", self.selection)
        self.bind("<Up>", self.moveUp)
        self.bind("<Down>", self.moveDown)
        
        self.listboxUp = False

    def changed(self, name, index, mode):
        if self.var.get() == '':
            if self.listboxUp:
                self.listbox.destroy()
                self.listboxUp = False
        else:
            words = self.comparison()
            if words:
                if not self.listboxUp:
                    self.listbox = Listbox(width=self["width"], height=self.listboxLength, justify='center')
                    self.listbox.bind("<Button-1>", self.selection)
                    self.listbox.bind("<Right>", self.selection)
                    self.listbox.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
                    self.listboxUp = True
                
                self.listbox.delete(0, END)
                for w in words:
                    self.listbox.insert(END,w)
            else:
                if self.listboxUp:
                    self.listbox.destroy()
                    self.listboxUp = False
        
    def selection(self, event):
        if self.listboxUp:
            self.var.set(self.listbox.get(ACTIVE))
            self.listbox.destroy()
            self.listboxUp = False
            self.icursor(END)

    def moveUp(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]
                
            if index != '0':                
                self.listbox.selection_clear(first=index)
                index = str(int(index) - 1)
                
                self.listbox.see(index) # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def moveDown(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]
                
            if index != END:                        
                self.listbox.selection_clear(first=index)
                index = str(int(index) + 1)
                
                self.listbox.see(index) # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index) 

    def comparison(self):
        return [ w for w in self.autocompleteList if self.matchesFunction(self.var.get(), w) ]


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


class popupWindow(object):
    def __init__(self,master):
        self.main_window = master
        top=self.top=Toplevel(master.raiz)
        top.resizable(width=False,height=False)
        top.geometry("230x100")
        top.title("Enter Size")
        top.wm_iconphoto(True, PhotoImage(data=icon))
        
        top.focus_force()
        top.grab_set()
        center(self.top)
        
        self.l=Label(top,text="Enter the desired size (In Hex)")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Save',command=self.cleanup,width=10)
        self.b.pack(pady=10)
        
    def cleanup(self):
        value=self.e.get()
        self.main_window.compress_file(value)
        self.top.destroy()

#=============================================
# File Management
#=============================================

def exists_in_file(file, string):
    file = open(file,'r')
    for line in file:
        line = line.strip()
        if string == line:
            file.close()
            return True
    else:
        file.close()
        return False

def replace_file(file,string):
    file = open(file,'w')
    file.write(string)
    file.close()

def append_to_file(file,string):
    file = open(file,'a')
    file.write(string+"\n")
    file.close()

def list_database(file):
    entries = []
    file = open(file,'r')
    for line in file:
        line = line.strip()
        entries.append(line)
    return entries

#=============================================
# Main Loop
#=============================================
        
class Application():
    
    def __init__(self):

        self.raiz = Tk()
        self.raiz.geometry('600x150')
        self.raiz.resizable(width=False,height=False)
        self.raiz.title('SmashScoreboard')
        self.score1 = 0
        self.score2 = 0
        self.score1_value = 0
        self.score2_value = 0
        self.player1_entry = ""
        self.player2_entry = ""
        self.round_entry = ""
        
        self.autocompletar = list_database("Database/players.txt")
        self.autocompletar_rounds = list_database("Database/rounds.txt")
        
        center(self.raiz)
        
        image = PhotoImage(data=photo)
        self.label = Label(image=image)
        self.label.image = image # keep a reference!
        self.label.grid(row=0,columnspan = 7, rowspan = 1)

        imgicon = PhotoImage(data=icon)
        self.raiz.call('wm', 'iconphoto', self.raiz._w, imgicon)

        Grid.rowconfigure(self.raiz, 0, weight=1)
        Grid.columnconfigure(self.raiz, 0, weight=1)

        #Create & Configure frame 
        frame=Frame(self.raiz)
        frame.grid(row=0, column=0, sticky=N+S+E+W)

        #Create a 5x7 (rows x columns) grid of buttons inside the frame
        for row_index in range(5):
            Grid.rowconfigure(frame, row_index, weight=1)
            for col_index in range(7):
                Grid.columnconfigure(frame, col_index, weight=1)
                tupla = (col_index, row_index)
                #row 0
                if tupla == (2,0) or tupla == (4,0):
                    label = Label(frame, text="Score")
                    label.grid(row=row_index, column=col_index, sticky=N+S+E+W)

                #row 1
                elif tupla == (0,1):
                    label = Label(frame, text="Player 1")
                    label.grid(row=row_index, column=col_index, sticky=N+S+E+W)
                elif tupla == (3,1):
                    label = Label(frame, text="Round")
                    label.grid(row=row_index, column=col_index, sticky=N+S+E+W)
                elif tupla == (6,1):
                    label = Label(frame, text="Player 2")
                    label.grid(row=row_index, column=col_index, sticky=N+S+E+W)  
                elif tupla == (1,1):
                    btn = Button(frame, text = "+", command = self.add_p1)
                    btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)
                elif tupla == (5,1):
                    btn = Button(frame, text = "+", command = self.add_p2)
                    btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)
                #row 2
                #Entry Players
                elif tupla == (0,2):
                    #self.player1_entry = Entry(frame)
                    self.player1_entry = AutocompleteEntry(self.autocompletar, frame, listboxLength=5, matchesFunction=matches, justify='center')
                    self.player1_entry.grid(row=row_index, column=col_index, sticky=N+S+E)
                elif tupla == (6,2):
                    #self.player2_entry = Entry(frame)
                    self.player2_entry= AutocompleteEntry(self.autocompletar, frame, listboxLength=5, matchesFunction=matches, justify='center')
                    self.player2_entry.grid(row=row_index, column=col_index, sticky=N+S+W)
                #Score Input
                elif tupla == (2,1):
                    self.score1_value = Entry(frame, bg="white", width = 1, font=("Calibri 50"), justify='center',state='disabled', disabledbackground="white", disabledforeground="black")
                    self.score1_value.grid(row=row_index, column=col_index, sticky=N+S+E+W, rowspan = 3)
                    self.score1_value.config(state=NORMAL)
                    self.score1_value.delete(0, END)
                    self.score1_value.insert(0, self.score1)
                    self.score1_value.config(state=DISABLED)
                elif tupla == (4,1):
                    self.score2_value = Entry(frame, bg="white", width = 1, font=("Calibri 50"), justify='center',state='disabled', disabledbackground="white", disabledforeground="black")
                    self.score2_value.grid(row=row_index, column=col_index, sticky=N+S+E+W, rowspan = 3)
                    self.score2_value.config(state=NORMAL)
                    self.score2_value.delete(0, END)
                    self.score2_value.insert(0, self.score1)
                    self.score2_value.config(state=DISABLED)
                #Score Resets
                elif tupla == (3,3):
                    btn = Button(frame, command = self.swap, text= "Swap Players")
                    btn.grid(row=row_index, column=col_index,padx=50, sticky=N+S+E+W)
                elif tupla == (1,2):
                    btn = Button(frame, text = "o", command = self.reset_p1, width = 3)
                    btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)
                elif tupla == (5,2):
                    btn = Button(frame, text = "o", command = self.reset_p2, width = 3)
                    btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)
                #Current Round
                elif tupla == (3,2):
                    #self.round_entry = Entry(frame, justify='center')
                    self.round_entry = AutocompleteEntry(self.autocompletar_rounds, frame, listboxLength=5, matchesFunction=matches, justify='center')
                    self.round_entry.grid(row=row_index, column=col_index, sticky=N+S+E+W, padx=20)
                #row 3
                #Score Resets

                elif tupla == (1,3):
                    btn = Button(frame, text = "-", command = self.substract_p1, width = 3)
                    btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)
                elif tupla == (5,3):
                    btn = Button(frame, text = "-", command = self.substract_p2)
                    btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)
                #row4
                #Save
                elif tupla == (3,4):
                    btn = Button(frame, text = "Update", command = self.save, width = 3, font = "Calibri 15")
                    btn.grid(row=row_index, column=col_index, sticky=N+S+E+W, padx= 40, pady = 10) 
                


        self.raiz.mainloop()

    def add_p1(self):
        self.score1 = min(9,self.score1+1)
        self.score1_value.config(state=NORMAL)
        self.score1_value.delete(0, END)
        self.score1_value.insert(0, self.score1)
        self.score1_value.config(state=DISABLED)
        
    def substract_p1(self):
        self.score1 = max(0,self.score1-1)
        self.score1_value.config(state=NORMAL)
        self.score1_value.delete(0, END)
        self.score1_value.insert(0, self.score1)
        self.score1_value.config(state=DISABLED)
        
    def reset_p1(self):
        self.score1 = 0
        self.score1_value.config(state=NORMAL)
        self.score1_value.delete(0, END)
        self.score1_value.insert(0, self.score1)
        self.score1_value.config(state=DISABLED)
        
    def add_p2(self):
        self.score2 = min(9,self.score2+1)
        self.score2_value.config(state=NORMAL)
        self.score2_value.delete(0, END)
        self.score2_value.insert(0, self.score2)
        self.score2_value.config(state=DISABLED)
        
    def substract_p2(self):
        self.score2 = max(0,self.score2-1)
        self.score2_value.config(state=NORMAL)
        self.score2_value.delete(0, END)
        self.score2_value.insert(0, self.score2)
        self.score2_value.config(state=DISABLED)
        
    def reset_p2(self):
        self.score2 = 0
        self.score2_value.config(state=NORMAL)
        self.score2_value.delete(0, END)
        self.score2_value.insert(0, self.score2)
        self.score2_value.config(state=DISABLED)
        
    def swap(self):
        p1_name = self.player1_entry.get()
        p1_score = self.score1_value.get()
        p2_name = self.player2_entry.get()
        p2_score = self.score2_value.get()

        #Reset p1
        self.score1_value.config(state=NORMAL)
        self.score1_value.delete(0, END)
        self.score1_value.insert(0, p2_score)
        self.score1_value.config(state=DISABLED)
        self.player1_entry.delete(0, END)
        self.player1_entry.insert(0, p2_name)

        #Reset p2
        self.score2_value.config(state=NORMAL)
        self.score2_value.delete(0, END)
        self.score2_value.insert(0, p1_score)
        self.score2_value.config(state=DISABLED)
        self.player2_entry.delete(0, END)
        self.player2_entry.insert(0, p1_name)
                                 
        return
    
    def save(self):
        p1_name = self.player1_entry.get()
        p1_score = self.score1_value.get()
        p2_name = self.player2_entry.get()
        p2_score = self.score2_value.get()
        current_round = self.round_entry.get()
        
        replace_file("Sources/player1.txt", p1_name)
        replace_file("Sources/player2.txt", p2_name)
        replace_file("Sources/score1.txt", p1_score)
        replace_file("Sources/score2.txt", p1_score)
        replace_file("Sources/round.txt", current_round)

        if not exists_in_file("Database/players.txt", p1_name):
            append_to_file("Database/players.txt", p1_name)
        if not exists_in_file("Database/players.txt", p2_name):
            append_to_file("Database/players.txt", p2_name)
        if not exists_in_file("Database/rounds.txt", current_round):
            append_to_file("Database/rounds.txt", current_round)
        self.autocompletar_rounds.append(current_round)
        self.autocompletar.append(p1_name)
        self.autocompletar.append(p2_name)
        return
 
def main():
    my_app = Application()
    return 0

if __name__ == '__main__':
    main()
