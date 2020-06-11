import dreamscript as ds
import tkinter as tk
from tkinter import Tk, scrolledtext, Menu, filedialog, messagebox, END
import sys
import re
from code import InteractiveConsole
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from runtime_result import *
from error import *
import runfile as rf 
import data_types as dt
import os

printretttt = ": )"
babu = 0

class History(list):
    def __getitem__(self, index):
        try:
            return list.__getitem__(self, index)
        except IndexError:
            return


class TextConsole(tk.Text):
    def __init__(self, master=None, **kw):
        font_specs = ("courier", 14)
        kw.setdefault('width', 83)
        kw.setdefault('height', 43)
        kw.setdefault('font', font_specs)
        kw.setdefault('wrap', 'word')
        kw.setdefault('prompt1', 'Dip> ')
        kw.setdefault('prompt2', '... ')
        banner = kw.pop('banner', "Dip Beta (Version 0.1)\nType in 'exit' to exit the shell\n\n")
        self._prompt1 = kw.pop('prompt1')
        self._prompt2 = kw.pop('prompt2')
        tk.Text.__init__(self, master, **kw)
        
        # --- history
        self.history = History()
        self._hist_item = 0
        self._hist_match = ''

        # --- initialization
        self._console = InteractiveConsole() # python console to execute commands
        self.insert('end', banner, 'banner')
        self.prompt()
        self.mark_set('input', 'insert')
        self.mark_gravity('input', 'left')

        # --- bindings
        self.bind('<Control-Return>', self.on_ctrl_return)
        self.bind('<Shift-Return>', self.on_shift_return)
        self.bind('<KeyPress>', self.on_key_press)
        self.bind('<KeyRelease>', self.on_key_release)
        self.bind('<Tab>', self.on_tab)
        self.bind('<Down>', self.on_down)
        self.bind('<Up>', self.on_up)
        self.bind('<Return>', self.on_return)
        self.bind('<BackSpace>', self.on_backspace)
        self.bind('<Control-c>', self.on_ctrl_c)
        self.bind('<<Paste>>', self.on_paste)

   
    def on_ctrl_c(self, event):
        """Copy selected code, removing prompts first"""
        sel = self.tag_ranges('sel')
        if sel:
            txt = self.get('sel.first', 'sel.last').splitlines()
            lines = []
            for i, line in enumerate(txt):
                if line.startswith(self._prompt1):
                    lines.append(line[len(self._prompt1):])
                elif line.startswith(self._prompt2):
                    lines.append(line[len(self._prompt2):])
                else:
                    lines.append(line)
            self.clipboard_clear()
            self.clipboard_append('\n'.join(lines))
        return 'break'

    def on_paste(self, event):
        """Paste commands"""
        if self.compare('insert', '<', 'input'):
            return "break"
        sel = self.tag_ranges('sel')
        if sel:
            self.delete('sel.first', 'sel.last')
        txt = self.clipboard_get()
        self.insert("insert", txt)
        self.insert_cmd(self.get("input", "end"))
        return 'break'

    def prompt(self, result=False):
        """Insert a prompt"""
        if result:
            self.insert('end', self._prompt2, 'prompt')
        else:
            self.insert('end', self._prompt1, 'prompt')
        self.mark_set('input', 'end-1c')

    def on_key_press(self, event):
        """Prevent text insertion in command history"""
        if self.compare('insert', '<', 'input') and event.keysym not in ['Left', 'Right']:
            self._hist_item = len(self.history)
            self.mark_set('insert', 'input lineend')
            if not event.char.isalnum():
                return 'break'

    def on_key_release(self, event):
        """Reset history scrolling"""
        if self.compare('insert', '<', 'input') and event.keysym not in ['Left', 'Right']:
            self._hist_item = len(self.history)
            return 'break'

    def on_up(self, event):
        """Handle up arrow key press"""
        if self.compare('insert', '<', 'input'):
            self.mark_set('insert', 'end')
            return 'break'
        elif self.index('input linestart') == self.index('insert linestart'):
            # navigate history
            line = self.get('input', 'insert')
            self._hist_match = line
            hist_item = self._hist_item
            self._hist_item -= 1
            item = self.history[self._hist_item]
            while self._hist_item >= 0 and not item.startswith(line):
                self._hist_item -= 1
                item = self.history[self._hist_item]
            if self._hist_item >= 0:
                index = self.index('insert')
                self.insert_cmd(item)
                self.mark_set('insert', index)
            else:
                self._hist_item = hist_item
            return 'break'

    def on_down(self, event):
        """Handle down arrow key press"""
        if self.compare('insert', '<', 'input'):
            self.mark_set('insert', 'end')
            return 'break'
        elif self.compare('insert lineend', '==', 'end-1c'):
            # navigate history
            line = self._hist_match
            self._hist_item += 1
            item = self.history[self._hist_item]
            while item is not None and not item.startswith(line):
                self._hist_item += 1
                item = self.history[self._hist_item]
            if item is not None:
                self.insert_cmd(item)
                self.mark_set('insert', 'input+%ic' % len(self._hist_match))
            else:
                self._hist_item = len(self.history)
                self.delete('input', 'end')
                self.insert('insert', line)
            return 'break'

    def on_tab(self, event):
        """Handle tab key press"""
        if self.compare('insert', '<', 'input'):
            self.mark_set('insert', 'input lineend')
            return "break"
        # indent code
        sel = self.tag_ranges('sel')
        if sel:
            start = str(self.index('sel.first'))
            end = str(self.index('sel.last'))
            start_line = int(start.split('.')[0])
            end_line = int(end.split('.')[0]) + 1
            for line in range(start_line, end_line):
                self.insert('%i.0' % line, '    ')
        else:
            txt = self.get('insert-1c')
            if not txt.isalnum() and txt != '.':
                self.insert('insert', '    ')
        return "break"

    def on_shift_return(self, event):
        """Handle Shift+Return key press"""
        if self.compare('insert', '<', 'input'):
            self.mark_set('insert', 'input lineend')
            return 'break'
        else: # execute commands
            self.mark_set('insert', 'end')
            self.insert('insert', '\n')
            self.insert('insert', self._prompt2, 'prompt')
            self.eval_current(True)

    def on_return(self, event=None):
        """Handle Return key press"""
        if self.compare('insert', '<', 'input'):
            self.mark_set('insert', 'input lineend')
            return 'break'
        else:
            self.eval_current(True)
            self.see('end')
        return 'break'

    def on_ctrl_return(self, event=None):
        """Handle Ctrl+Return key press"""
        self.insert('insert', '\n' + self._prompt2, 'prompt')
        return 'break'

    def on_backspace(self, event):
        """Handle delete key press"""
        if self.compare('insert', '<=', 'input'):
            self.mark_set('insert', 'input lineend')
            return 'break'
        sel = self.tag_ranges('sel')
        if sel:
            self.delete('sel.first', 'sel.last')
        else:
            linestart = self.get('insert linestart', 'insert')
            if re.search(r'    $', linestart):
                self.delete('insert-4c', 'insert')
            else:
                self.delete('insert-1c')
        return 'break'

    def insert_cmd(self, cmd):
        """Insert lines of code, adding prompts"""
        input_index = self.index('input')
        self.delete('input', 'end')
        lines = cmd.splitlines()
        if lines:
            indent = len(re.search(r'^( )*', lines[0]).group())
            self.insert('insert', lines[0][indent:])
            for line in lines[1:]:
                line = line[indent:]
                self.insert('insert', '\n')
                self.prompt(True)
                self.insert('insert', line)
                self.mark_set('input', input_index)
        self.see('end')
    

    
    def eval_current(self, auto_indent=False):
        
        """Evaluate code"""
        index = self.index('input')
        lines = self.get('input', 'insert lineend').splitlines() # commands to execute
        self.mark_set('insert', 'insert lineend')
        if lines:  # there is code to execute
            # remove prompts
            lines = [lines[0].rstrip()] + [line[len(self._prompt2):].rstrip() for line in lines[1:]]
            cmds = '\n'.join(lines)
            self.insert('insert', '\n')
            if cmds == 'exit':
                exit()

            result, error = ds.run('<Dip Shell>', cmds)
            
            if error:
                self.insert('insert', '\n')
                error_as_string = error.as_string()
                bear = """\n .------.
(        )    ..
 `------'   .' /
      O    /  ;
        o i  OO
         C    `-.
         |    <-'
         (  ,--.
          V  \_)
           \  :
            `._\.
\n"""

              
                self.insert('insert', error_as_string)
                self.insert('insert', f'{bear}\n')
                self.insert('insert', '\n')
                self.prompt()

            if dt.veryimp == 1:
                for i in dt.toprint:
                    if i == "pr":
                        continue
                    result.elements.append(i)
                    self.insert('insert', f'{i}\n')
            for i in result.elements:
                print(i)
                if i == "" or i == "pr" or i in dt.toprint:
                    continue
                self.insert('insert', f'{i}\n')
            self.prompt()
            dt.toprint = []

            dt.veryimp = 0
    
        else:
            self.insert('insert', '\n')
            self.prompt()


        
                
        

class Menubar:

    def __init__(self, parent):
        font_specs = ("sans", 14)

        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label="New File",
                                  accelerator="Cmd+N",
                                  command=parent.new_file)
        file_dropdown.add_command(label="Open File",
                                  accelerator="Cmd+O",
                                  command=parent.open_file)
        file_dropdown.add_command(label="Save",
                                  accelerator="Cmd+S",
                                  command=parent.save)
        file_dropdown.add_command(label="Save As",
                                  accelerator="Cmd+Shift+S",
                                  command=parent.save_as)
        file_dropdown.add_command(label="Run",
                                  accelerator="Cmd+R",
                                  command=parent.run)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit",
                                  command=parent.master.destroy)

        about_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        about_dropdown.add_command(label="Release Notes",
                                   command=self.show_release_notes)
        about_dropdown.add_separator()
        about_dropdown.add_command(label="About",
                                   command=self.show_about_message)

        menubar.add_cascade(label="File", menu=file_dropdown)
        menubar.add_cascade(label="About", menu=about_dropdown)

    def show_about_message(self):
        box_title = "About Dip"
        box_message = "The DDE - or dip development environment!"
        messagebox.showinfo(box_title, box_message)

    def show_release_notes(self):
        box_title = "Release Notes"
        box_message = "Dip - Beta"
        messagebox.showinfo(box_title, box_message)
            


class Statusbar:

    def __init__(self, parent):

        font_specs = ("courier", 12,)
        
        self.status = tk.StringVar()
        self.status.set("Dip - Beta")

        label = tk.Label(parent.textarea, textvariable=self.status, fg="black",
                         bg="lightgrey", anchor='sw', font=font_specs)
        label.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def update_status(self, *args):
        if isinstance(args[0], bool):
            self.status.set("Your File Has Been Saved!")
        else:
            self.status.set("Dip - Beta")


class DreamText: 

    def __init__(self, master=None): 
        if master:
            master.title("Untitled - Dip")
            master.geometry("1200x700")     

            font_specs = ("courier", 14)

            self.master = master
            self.filename = None

            self.textarea = tk.Text(master, font=font_specs)
            self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
            self.textarea.configure(yscrollcommand=self.scroll.set)
            self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

            self.menubar = Menubar(self)
            self.statusbar = Statusbar(self)

            self.bind_shortcuts()

    def set_window_title(self, name=None):
        if name:
            self.master.title(name + " - Dip")
        else:
            self.master.title("Untitled - Dip")

    def new_file(self, *args):
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()

    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension=".dip",
            filetypes=[("Dip Files", "*.dip")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
            self.set_window_title(self.filename)
    
    def save(self, *args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
                self.statusbar.update_status(True)
            except Exception as e:
                print(e)
        else:
            self.save_as()
    
    def run(self):
        box_title = "Run"
        box_message = 'To run a program, type run("path/to/your/script") in the prompt'
        messagebox.showinfo(box_title, box_message)

          
    def save_as(self, *args):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.dip",
                defaultextension=".dip",
                filetypes=[("Dip Files", "*.dip")])
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
            self.statusbar.update_status(True)
        except Exception as e:
            print(e)

    def bind_shortcuts(self):
        self.textarea.bind('<Command-n>', self.new_file)
        self.textarea.bind('<Command-o>', self.open_file)
        self.textarea.bind('<Command-s>', self.save)
        self.textarea.bind('<Command-R>', self.run)
        self.textarea.bind('<Key>', self.statusbar.update_status)
    
    


class Main:
    def __init__(self):
        self.printret = []
        self.toprint = False
        self.runvar = False
    def changevars(self, changedprintret, changedtoprint, changedrunvar):
        self.printret.append(changedprintret)
        self.toprint = changedtoprint
        self.runvar = changedrunvar
    def show(self):
        return self.printret, self.toprint, self.runvar



def maindef():
        root = tk.Tk()
        console = TextConsole(root)
        dt = DreamText(root)
        console.pack(fill='both', expand=True)
        main = Main()
        
        root.mainloop()  

if __name__ == '__main__':
    maindef()
