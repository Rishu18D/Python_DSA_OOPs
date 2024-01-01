import tkinter as TK 
root=TK.Tk()
L1=TK.Label(root,text="hello world!!!!")
b1=TK.Button(root,text="okay")
b2=TK.Button(root,{"text":"cancel"})

b1.pack()
b2.pack()
L1.pack()
root.mainloop()