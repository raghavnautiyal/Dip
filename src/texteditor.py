from tkinter import Tk, scrolledtext, Menu, filedialog, messagebox, Toplevel, Label

root = Tk(className= " Dreamscript Editor")
textArea = scrolledtext.ScrolledText(width = 500, height = 500)

def newFile():
    if len(textArea.get('1.0', 'end' + '-1c')) > 0:
        if messagebox.askyesno("Save", "Do you wish to save?"):
            saveFile()
    newWindow = Toplevel(scrolledtext.ScrolledText(width = 500, height = 500))
    newWindow.title("Dreamscript Editor")
    newWindow.geometry("500x500")  
    newWindow.textArea = scrolledtext.ScrolledText(width = 500, height = 500)
    menu = Menu(root)
    root.config(menu=menu)
    fileMenu = Menu(menu)
    menu.add_cascade(label="File", menu = fileMenu)
    fileMenu.add_command(label="New File", command=newFile)
    fileMenu.add_command(label="Open...", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Quit", command=exitRoot)

    helpMenu = Menu(menu)
    menu.add_cascade(label="Help", menu = helpMenu)

    abtmenu = Menu(menu)
    menu.add_cascade(label="About",  menu = abtmenu)
    menu.add_cascade(label="About",  command = about)

    root.mainloop()
    
  


def openFile():
    file = filedialog.askopenfile(parent=root, title='Select a .drm file', filetypes=(("Dreamscript File", "*.drm"),))

    if file != None:
        contents = file.read()
        textArea.insert('1.0', contents)
        file.close()


def saveFile():
    file = filedialog.asksaveasfile(mode='w')

    if file != None:
        data = textArea.get('1.0', 'end' + '-1c')
        file.write(data)
        file.close()
def about():
    label = messagebox.showinfo('About', "Dreamscript Beta (Version 0.1) - Shell\n Developed by Raghav Nautiyal with love!")

def exitRoot():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()

# Menu Options

menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu = fileMenu)
fileMenu.add_command(label="New File", command=newFile)
fileMenu.add_command(label="Open...", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Quit", command=exitRoot)
textArea.pack()

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu = helpMenu)

abtmenu = Menu(menu)
menu.add_cascade(label="About",  menu = abtmenu)
menu.add_cascade(label="About",  command = about)

root.mainloop()